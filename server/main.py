from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)
cors = CORS(app, origins='*')

# Load the model and label encoders globally
xgb_model = joblib.load('xgb_traffic_model.joblib')
le_road = joblib.load('le_road.joblib')
le_weather = joblib.load('le_weather.joblib')

# Endpoint to get road names
@app.route("/api/road_names", methods=['GET'])
def road_names():
    try:
        road_data = pd.read_csv("Data/Road_List.csv")
        road_names = road_data['Name of Road'].tolist()
        return jsonify({"road_names": road_names})
    except FileNotFoundError:
        print("Error: road_list.csv file not found. Returning empty list.")
        return jsonify({"error": "File not found"})
    except Exception as e:
        print(f"Error reading road_list.csv: {e}")
        return jsonify({"error": str(e)})

# Traffic prediction function
def predict_traffic_xgb(road_name, future_date, weather_condition='normal'):
    # Convert inputs to model features
    if road_name in le_road.classes_:
        road_encoded = le_road.transform([road_name])[0]
    else:
        print(f"Warning: '{road_name}' is an unseen road name. Using -1 as a placeholder.")
        road_encoded = -1

    date = pd.to_datetime(future_date)

    if weather_condition in le_weather.classes_:
        weather_encoded = le_weather.transform([weather_condition])[0]
    else:
        print(f"Warning: '{weather_condition}' is an unseen weather condition. Using the most frequent condition.")
        weather_encoded = le_weather.transform([le_weather.classes_[0]])[0]

    # Create feature vector (adjust this based on your actual features)
    features = [
        road_encoded, 
        date.month, 
        date.dayofweek, 
        int(date.dayofweek in [5, 6]),  # IsWeekend
        0, 0, 0, 0, 0, 0, 0, 0,  # Placeholder values for other features
        weather_encoded,
        0  # Placeholder for 'Roadwork and Construction Activity'
    ]
    
    # Make prediction
    X = np.array(features).reshape(1, -1)
    prediction = xgb_model.predict(X)
    
    return prediction[0]

# Endpoint for traffic prediction
@app.route('/api/predict_traffic', methods=['POST'])
def predict_traffic():
    try:
        # Get JSON data from request
        data = request.get_json()
        road_name = data['road_name']
        future_date = data['future_date']
        weather_condition = data.get('weather_condition', 'normal')

        # Make prediction
        predicted_traffic = predict_traffic_xgb(road_name, future_date, weather_condition)

        # Convert numpy.float32 to float
        predicted_traffic = float(predicted_traffic)

        # Return prediction as JSON response
        return jsonify({'predicted_traffic_volume': predicted_traffic})

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True, port=8081)
