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
from flask import redirect,url_for
from flask import Flask, render_template
import plotly.offline as pyo
import plotly.graph_objs as go
app = Flask(__name__)
import io
import random
from flask import Flask, render_template, request, redirect, url_for, session, flash
import base64
from PIL import Image
import numpy as np
from flask import Flask, render_template, request, jsonify
import plotly.offline as pyo
import plotly.graph_objs as go
from get_wallpapers import get_wallpapers
#model = joblib.load('path/to/saved/model.pkl')
@app.route('/')
def home():
    #return 'Hello, World!'
    data = [1, 2, 3, 4, 5]
    plot_div = pyo.plot(create_plot(), output_type='div')
    if 'logged_in' in session and session['logged_in']:
        return render_template('index.html',data=data, plot_div=plot_div)
    else:
        return redirect(url_for('login'))
app.secret_key = 'lifeisgood'

# Define a route to handle predictions
#@app.route('/predict', methods=['POST'])
def predict():
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
    return jsonify({'prediction': prediction_str})
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
# Create instance of LoginManager
login_manager = LoginManager(app)

# Create a User class that inherits from UserMixin
class User(UserMixin):
    pass

# Set up a user_loader function to load a user from a user_id
@login_manager.user_loader
def load_user(user_id):
    # In this example, we're just using a single user with the username 'admin' and password 'password'
    if user_id == 'admin':
        user = User()
        user.id = user_id
        return user
    return None

# Add a login route to authenticate users
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            user = User()
            user.id = username
            login_user(user)
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')
    image_urls = get_wallpapers()

    # Choose a random image URL from the list
    random_wallpaper = image_urls[random.randint(0, len(image_urls) - 1)]
    return render_template('login.html', wallpaper=random_wallpaper)

# Add a logout route to log out users
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Add a current_user route to get the current user
@app.route('/current_user')
def current_user():
    if current_user.is_authenticated:
        return jsonify({'username': current_user.id})
    else:
        return jsonify({'username': 'anonymous'})

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
@app.route('/classify', methods=['POST'])
def classify():
    # Get the image data from the form
    image = request.files['image'].read()

    # Use the cow detector to predict whether the image contains a cow
    prediction = cow_detector.predict_cow(image)

    # Render the prediction template with the prediction result
    return render_template('prediction.html', prediction=prediction)
if __name__ == '__main__':
    app.run(debug=True)