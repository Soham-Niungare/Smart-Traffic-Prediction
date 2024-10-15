from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
cors = CORS(app, origins='*')


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


if __name__ == "__main__":
    app.run(debug=True, port=8080)