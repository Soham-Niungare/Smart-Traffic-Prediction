from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from keras.models import load_model
from datetime import datetime
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load your trained LSTM model
model = load_model('../traffic_volume_model.h5')

# Load the dataset for road names
data = pd.read_csv("Road_List.csv")  # Update path as needed
road_names = data['Name of Road'].tolist()


df = pd.read_csv("Traffic_Data_5.csv")
# Check unique road names
print("Unique road names in the dataset:", df['Road/Intersection Name'].unique())

# Check unique dates
print("Unique dates in the dataset:", df['Date'].unique())

# # Encode the road names using LabelEncoder
# label_encoder = LabelEncoder()
# road_names_encoded = label_encoder.fit_transform(road_names)

# def preprocess_date(date_str):
#     date_obj = datetime.strptime(date_str, "%Y-%m-%d")
#     day_of_week = date_obj.weekday()  # Monday=0, Sunday=6
#     is_weekend = 1 if day_of_week >= 5 else 0  # 1 for Saturday/Sunday, 0 for other days
#     return [day_of_week, is_weekend]

# @app.route("/")
# def index():
#     return render_template('index.html', road_names=road_names)

# @app.route('/predict', methods=['POST'])
# def predict():
#     road_name = request.form.get('road_names')
#     date = request.form.get('date')

#     # Check if road_name is None or not in the list
#     if road_name is None or road_name not in road_names:
#         return "Error: Road name is not valid."

#     # Encode the road name using the LabelEncoder
#     try:
#         road_name_encoded = label_encoder.transform([road_name])[0]
#     except ValueError:
#         return "Error: Unseen road name provided."

#     # Preprocess the date
#     features = preprocess_date(date)

#     # Prepare the input array for the model (ensure proper reshaping for LSTM)
#     input_array = np.array([[road_name_encoded] + features])
#     input_array = np.reshape(input_array, (1, 1, len(input_array[0])))  # Reshape to 3D if needed by LSTM

#     # Make a prediction
#     prediction = model.predict(input_array)

#     # Assuming your model outputs a normalized traffic volume, scale it back to the original range
#     predicted_volume = prediction[0][0] * 105849  # Adjust this scaling factor based on your dataset

#     return str(np.round(predicted_volume, 2))  # Return rounded prediction

# if __name__ == "__main__":
#     app.run(debug=True, port=3000)


