import json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.preprocessing import MinMaxScaler

# Define parameters
df_roads = pd.read_csv('Road_List.csv')
roads = df_roads["Name of Road"].tolist()
holidays = [
    "2022-01-01", "2022-01-26", "2022-02-05", "2022-03-01",
    "2022-04-10", "2022-04-14", "2022-05-01", "2022-05-03",
    "2022-06-14", "2022-08-15", "2022-08-19", "2022-10-02",
    "2022-10-24", "2022-11-05", "2022-12-25"
]

# Festival data
with open('festival_data.json', 'r') as f:
    festival_data = json.load(f)

print("Festival data loaded from festival_data.json")

# Function to determine weather based on date and season
def get_weather_condition(date):
    month = date.month
    if 3 <= month <= 5:  # Summer: March to May
        weather = np.random.choice(["Hot and Humid", "Clear", "Heatwave"], p=[0.6, 0.3, 0.1])
    elif 6 <= month <= 9:  # Monsoon: June to September
        weather = np.random.choice(["Rainy", "Thunderstorm", "Clear"], p=[0.7, 0.2, 0.1])
    elif 10 <= month <= 12 or 1 <= month <= 2:  # Winter: October to February
        weather = np.random.choice(["Mild", "Fog", "Clear"], p=[0.7, 0.2, 0.1])
    return weather

# Function to generate festival multipliers for a given date
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

# Generate dates for the year 2022
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)
date_range = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]

# Function to handle missing or erroneous data
def handle_missing_data(value, lower_bound, upper_bound):
    if pd.isna(value) or value < lower_bound or value > upper_bound:
        return np.random.uniform(lower_bound, upper_bound)  # Fill with a random value in the valid range
    return value

# Function to generate random traffic data for each road on each date
def generate_traffic_data(date, road, weather, traffic_multiplier, pedestrian_multiplier):
    is_weekend = date.weekday() >= 5  # Check if it's a weekend
    is_holiday = date.strftime('%Y-%m-%d') in holidays  # Check if it's a holiday
    
    # Generate traffic volume with some variability
    base_volume = np.random.randint(30000, 60000)
    traffic_volume = base_volume + np.random.randint(-5000, 5000) if not is_weekend else base_volume - np.random.randint(0, 10000)
    traffic_volume = int(traffic_volume * traffic_multiplier)  # Apply festival traffic multiplier
    
    # Generate initial metrics
    avg_speed = np.random.uniform(20, 60)
    travel_time_index = np.random.uniform(1, 2)
    congestion_level = np.random.randint(0, 100)
    road_capacity_utilization = np.random.uniform(50, 100)
    incident_reports = np.random.randint(0, 5)
    environmental_impact = np.random.uniform(50, 100)
    public_transport_usage = np.random.uniform(10, 50)
    traffic_signal_compliance = np.random.uniform(80, 100)
    parking_usage = np.random.uniform(0, 100)
    
    # Apply dependency adjustments
    congestion_level += incident_reports * 5
    congestion_level += (road_capacity_utilization - 80) / 2 if road_capacity_utilization > 80 else 0

    travel_time_index = 1 + (congestion_level / 100) + (incident_reports * 0.1)
    avg_speed = max(10, avg_speed - (congestion_level / 2) - (incident_reports * 2))

    traffic_volume -= public_transport_usage * 100
    environmental_impact += (traffic_volume - 30000) / 3000

    pedestrian_and_cyclist_count = int(np.random.randint(0, 100) * pedestrian_multiplier) + int(public_transport_usage * 1.5)

    if traffic_signal_compliance < 85 and np.random.rand() > 0.5:
        incident_reports += 1
    
    # Ensure values are within expected ranges using missing data handling function
    avg_speed = handle_missing_data(avg_speed, 10, 60)
    congestion_level = handle_missing_data(congestion_level, 0, 100)
    traffic_volume = handle_missing_data(traffic_volume, 0, 100000)
    environmental_impact = handle_missing_data(environmental_impact, 50, 150)

    # Return traffic data for the specific road and date
    return [
        date.strftime('%d-%m-%Y'), road, traffic_volume, avg_speed, travel_time_index,
        congestion_level, road_capacity_utilization, incident_reports, environmental_impact,
        public_transport_usage, traffic_signal_compliance, parking_usage,
        pedestrian_and_cyclist_count, weather, np.random.randint(0, 2)
    ]

# Now, generate data for every road for each date (optimize by moving weather and festival multiplier calculation outside inner loop)
data = []
for date in date_range:
    weather = get_weather_condition(date)  # Calculate weather once per date
    festival_multipliers = get_festival_multiplier_for_date(date)  # Get festival multipliers for date
    for road in roads:
        traffic_multiplier, pedestrian_multiplier = festival_multipliers.get(road, (1, 1))  # Lookup in dictionary
        data.append(generate_traffic_data(date, road, weather, traffic_multiplier, pedestrian_multiplier))

# Create the DataFrame
columns = ["Date", "Road/Intersection Name", "Traffic Volume", "Average Speed", "Travel Time Index", 
           "Congestion Level", "Road Capacity Utilization", "Incident Reports", "Environmental Impact", 
           "Public Transport Usage", "Traffic Signal Compliance", "Parking Usage", 
           "Pedestrian and Cyclist Count", "Weather Conditions", "Roadwork and Construction Activity"]
df = pd.DataFrame(data, columns=columns)

# Feature normalization using MinMaxScaler
scaler = MinMaxScaler()
numerical_columns = ["Traffic Volume", "Average Speed", "Travel Time Index", "Congestion Level",
                     "Road Capacity Utilization", "Incident Reports", "Environmental Impact", 
                     "Public Transport Usage", "Traffic Signal Compliance", "Parking Usage", 
                     "Pedestrian and Cyclist Count"]

df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

# Save the DataFrame to CSV
df.to_csv('Traffic_Data_Normalized.csv', index=False)

print("Traffic data generation and normalization complete!")
