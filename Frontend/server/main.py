from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
cors = CORS(app, origins='*')

# Endpoint to get road names
@app.route("/api/road_names", methods=['GET'])
def road_names():
    try:
        road_data = pd.read_csv("Road_List.csv")
        road_names = road_data['Name of Road'].tolist()
        return jsonify({"road_names": road_names})
    except FileNotFoundError:
        print("Error: road_list.csv file not found. Returning empty list.")
        return jsonify({"error": "File not found"})
    except Exception as e:
        print(f"Error reading road_list.csv: {e}")
        return jsonify({"error": str(e)})

# New endpoint to handle prediction requests and print the variables
@app.route('/api/predict_traffic', methods=['POST'])
def predict_traffic():
    try:
        # Get the JSON data sent from the frontend
        data = request.get_json()
        
        # Extract the values from the JSON data
        road_name = data.get('road_name')
        future_date = data.get('future_date')
        weather_condition = data.get('weather_condition', 'normal')

        # Print the values to the terminal
        print(f"Received road_name: {road_name}")
        print(f"Received future_date: {future_date}")
        print(f"Received weather_condition: {weather_condition}")
        
        # Dummy response (you can replace this with a prediction later)
        return jsonify({
            'road_name': road_name,
            'future_date': future_date,
            'weather_condition': weather_condition,
            'prediction': 'This is a dummy prediction for now'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=8080)
