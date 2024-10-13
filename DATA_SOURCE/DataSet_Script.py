import json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.preprocessing import MinMaxScaler

# Load road list and festival data
df_roads = pd.read_csv('Road_List.csv')
roads = df_roads["Name of Road"].tolist()

# Define public holidays
holidays = [
    "2022-01-01", "2022-01-26", "2022-02-05", "2022-03-01",
    "2022-04-10", "2022-04-14", "2022-05-01", "2022-05-03",
    "2022-06-14", "2022-08-15", "2022-08-19", "2022-10-02",
    "2022-10-24", "2022-11-05", "2022-12-25"
]

# Load festival data from JSON file
with open('festival_data.json', 'r') as f:
    festival_data = json.load(f)

print("Festival data loaded successfully")

# Function to determine weather conditions based on season
def get_weather_condition(date):
    month = date.month
    if 3 <= month <= 5:  # Summer: March to May
        return np.random.choice(["Hot and Humid", "Clear", "Heatwave"], p=[0.6, 0.3, 0.1])
    elif 6 <= month <= 9:  # Monsoon: June to September
        return np.random.choice(["Rainy", "Thunderstorm", "Clear"], p=[0.7, 0.2, 0.1])
    else:  # Winter: October to February
        return np.random.choice(["Mild", "Fog", "Clear"], p=[0.7, 0.2, 0.1])

# Function to get festival multipliers for a specific date
def get_festival_multiplier_for_date(date):
    multiplier_map = {}
    for festival, details in festival_data.items():
        for start, end in details["date_range"]:
            start_date = datetime.strptime(start, "%Y-%m-%d")
            end_date = datetime.strptime(end, "%Y-%m-%d")
            if start_date <= date <= end_date:
                for area in details["affected_areas"]:
                    multiplier_map[area] = (details["traffic_increase"], details["pedestrian_increase"])
    return multiplier_map

# Function to handle missing or out-of-bound data
def handle_missing_data(value, lower_bound, upper_bound):
    if pd.isna(value) or value < lower_bound or value > upper_bound:
        return np.random.uniform(lower_bound, upper_bound)
    return value

# Function to introduce random missing values into the dataset
def introduce_random_missing_values(df, missing_percentage=0.1):
    df_with_missing = df.copy()
    total_entries = df_with_missing.size
    num_missing = int(missing_percentage * total_entries)
    
    for _ in range(num_missing):
        row_idx = np.random.randint(0, df_with_missing.shape[0])
        col_idx = np.random.randint(0, df_with_missing.shape[1])
        df_with_missing.iat[row_idx, col_idx] = np.nan
    
    return df_with_missing

# Function to generate random traffic data
def generate_traffic_data(date, road, weather, traffic_multiplier, pedestrian_multiplier):
    is_weekend = date.weekday() >= 5
    is_holiday = date.strftime('%Y-%m-%d') in holidays
    
    base_volume = np.random.randint(30000, 60000)
    traffic_volume = base_volume + np.random.randint(-5000, 5000) if not is_weekend else base_volume - np.random.randint(0, 10000)
    traffic_volume = int(traffic_volume * traffic_multiplier)
    
    avg_speed = np.random.uniform(20, 60)
    travel_time_index = np.random.uniform(1, 2)
    congestion_level = np.random.randint(0, 100)
    road_capacity_utilization = np.random.uniform(50, 100)
    incident_reports = np.random.randint(0, 5)
    environmental_impact = np.random.uniform(50, 100)
    public_transport_usage = np.random.uniform(10, 50)
    
    congestion_level += (traffic_volume - 30000) / 10000
    congestion_level += incident_reports * 5
    congestion_level += (road_capacity_utilization - 80) / 2 if road_capacity_utilization > 80 else 0

    travel_time_index = 1 + (congestion_level / 100) + (incident_reports * 0.1)
    avg_speed = max(10, avg_speed - (congestion_level / 2) - (incident_reports * 2))
    
    traffic_volume -= public_transport_usage * 100
    environmental_impact += (traffic_volume - 30000) / 3000
    environmental_impact += (congestion_level / 20)
    environmental_impact -= (public_transport_usage / 10)
    
    pedestrian_and_cyclist_count = int(np.random.randint(0, 100) * pedestrian_multiplier) + int(public_transport_usage * 1.5)
    
    if np.random.rand() < 0.5 and public_transport_usage < 30:
        incident_reports += 1
    
    # Handle missing or erroneous data
    avg_speed = handle_missing_data(avg_speed, 10, 60)
    congestion_level = handle_missing_data(congestion_level, 0, 100)
    traffic_volume = handle_missing_data(traffic_volume, 0, 100000)
    environmental_impact = handle_missing_data(environmental_impact, 50, 150)
    
    return [
        date.strftime('%d-%m-%Y'), road, traffic_volume, avg_speed, travel_time_index,
        congestion_level, road_capacity_utilization, incident_reports, environmental_impact,
        public_transport_usage, pedestrian_and_cyclist_count, weather, np.random.randint(0, 2)
    ]

# Generate traffic data for each date and road
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)
date_range = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]

data = []
for date in date_range:
    weather = get_weather_condition(date)
    festival_multipliers = get_festival_multiplier_for_date(date)
    for road in roads:
        traffic_multiplier, pedestrian_multiplier = festival_multipliers.get(road, (1, 1))
        data.append(generate_traffic_data(date, road, weather, traffic_multiplier, pedestrian_multiplier))

# Create a DataFrame
columns = [
    "Date", "Road/Intersection Name", "Traffic Volume", "Average Speed", "Travel Time Index", 
    "Congestion Level", "Road Capacity Utilization", "Incident Reports", "Environmental Impact", 
    "Public Transport Usage", "Pedestrian and Cyclist Count", "Weather Conditions", 
    "Roadwork and Construction Activity"
]
df = pd.DataFrame(data, columns=columns)

# Introduce missing values
df = introduce_random_missing_values(df, missing_percentage=0.1)
print("Missing values introduced.")

# Normalize numerical columns
numerical_columns = [
    "Traffic Volume", "Average Speed", "Travel Time Index", "Congestion Level",
    "Road Capacity Utilization", "Incident Reports", "Environmental Impact", 
    "Public Transport Usage", "Pedestrian and Cyclist Count"
]
scaler = MinMaxScaler()
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

# Save to CSV
df.to_csv('Traffic_Data_4.csv', index=False)
print("Traffic data generation complete and saved to 'Traffic_Data_4.csv'.")
