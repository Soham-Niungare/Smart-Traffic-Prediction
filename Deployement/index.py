from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from keras.models import load_model
from datetime import datetime

app = Flask(__name__)

# Load your trained LSTM model
model = load_model('../traffic_volume_model.h5')

# Load the dataset for road names
data = pd.read_csv("Road_List.csv")  # Update path as needed
road_names = data['Name of Road'].tolist()  # Replace 'Address' with the actual column name for roads
def preprocess_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    day_of_week = date_obj.weekday()  # Monday=0, Sunday=6
    is_weekend = 1 if day_of_week >= 5 else 0  # 1 for Saturday/Sunday, 0 for other days

    return [day_of_week, is_weekend]

@app.route("/")
def index():
    return render_template('index.html', road_names=road_names)

@app.route('/predict', methods=['POST'])
def predict():
    road_name = request.form.get('road_names')
    date = request.form.get('date')


    # Preprocess the date
    features = preprocess_date(date)

    # Prepare the input array for the model
    input_array = np.array([[road_name] + features])
    
    # Make a prediction
    prediction = model.predict(input_array)

    # Assuming your model outputs a normalized traffic volume, scale it back to the original range
    # Use the max traffic volume from your data for scaling (replace 105849 with actual max)
    predicted_volume = prediction[0][0] * 105849  # Change 105849 to the actual max volume from your dataset

    return str(np.round(predicted_volume, 2))  # Return rounded prediction

if __name__ == "__main__":
    app.run(debug=True, port=3000)
