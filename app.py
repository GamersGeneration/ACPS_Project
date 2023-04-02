#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rePUBLIC
#
# Created:     01-04-2023
# Copyright:   (c) rePUBLIC 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from flask import Flask, render_template
import plotly.offline as pyo
import plotly.graph_objs as go
app = Flask(__name__)
import io
import base64
from PIL import Image
import numpy as np
from flask import Flask, render_template, request, jsonify
import plotly.offline as pyo
import plotly.graph_objs as go

from cow_detector import predict_cow
#model = joblib.load('path/to/saved/model.pkl')
@app.route('/')
def home():
    #return 'Hello, World!'
    data = [1, 2, 3, 4, 5]
    plot_div = pyo.plot(create_plot(), output_type='div')
    return render_template('index.html',data=data, plot_div=plot_div)

"""def preprocess_image(image):
    # Convert the image to grayscale
    image = image.convert('L')
    # Resize the image to 128x128
    image = image.resize((128, 128))
    # Convert the image to a NumPy array
    image_array = np.array(image)
    # Normalize the image
    image_array = image_array / 255.0
    # Add a batch dimension to the image
    image_array = np.expand_dims(image_array, axis=0)
    return image_array
"""
# Define a route to handle predictions
#@app.route('/predict', methods=['POST'])
"""def predict():
    # Get the image file from the request
    image_file = request.files['image']
    # Read the image file into a PIL Image object
    image = Image.open(io.BytesIO(image_file.read()))
    # Preprocess the image
    image_array = preprocess_image(image)
    # Use the model to make a prediction
    prediction = model.predict(image_array)[0]
    # Convert the prediction to a string
    prediction_str = 'Cow' if prediction == 1 else 'Not Cow'
    # Return the prediction as a JSON object
    return jsonify({'prediction': prediction_str})"""
@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'})
    image = request.files['image'].read()
    prediction = predict_cow(image)
    return jsonify({'prediction': prediction})
def create_plot():
    trace = go.Bar(x=['Mon', 'Tue', 'Wed'], y=[1, 2, 3])
    layout = go.Layout(title='Buzzer Frequency')
    fig = go.Figure(data=[trace], layout=layout)
    return fig
if __name__ == '__main__':
    app.run(debug=True)