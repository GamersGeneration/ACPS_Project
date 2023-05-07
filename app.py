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
from flask import redirect,url_for, send_from_directory
import os
import pickle
from flask import Flask, render_template
import plotly.offline as pyo
import plotly.graph_objs as go
UPLOAD_FOLDER = "C:/Users/rePUBLIC/Desktop/test"
app = Flask(__name__, template_folder='templates', static_folder='static')
import io
import random
import joblib
import tensorflow
from flask import Flask, render_template, request
import classifier

from werkzeug.utils import secure_filename

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#import cv2
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, session, flash
import base64
from PIL import Image
import numpy as np
from flask import Flask, render_template, request, jsonify
import plotly.offline as pyo
import plotly.graph_objs as go
from get_wallpapers import get_wallpapers
from classifier import getPrediction
#model = joblib.load('path/to/saved/model.pkl')
@app.route('/')
@app.route('/home')
def home():
    #return 'Hello, World!'
    data = [1, 2, 3, 4, 5]
    plot_div = pyo.plot(create_plot(), output_type='div')
    #if 'logged_in' in session and session['logged_in']:
    return render_template('index.html')
    #else:
        #return redirect(url_for('login'))
app.secret_key = 'lifeisgood'




# Loading the ML model into Flask
#model = load_model('model.h5')




# Define a route to handle predictions

"""from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
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


    # Choose a random image URL from the list
    return render_template('login.html')

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
        return jsonify({'username': 'anonymous'})"""
@app.route('/predict', methods=['GET', 'POST'])
def submit_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            getPrediction(filename)
            label, acc = getPrediction(filename)
            flash(label)
            flash(acc)
            flash(filename)
            return render_template('predict.html')
@app.route('/upload')
def upload():
    return render_template('upload.htm')
def create_plot():
    trace = go.Bar(x=['Mon', 'Tue', 'Wed'], y=[1, 2, 3])
    layout = go.Layout(title='Buzzer Frequency')
    fig = go.Figure(data=[trace], layout=layout)
    return fig
#@app.route('/course')
#@app.route('/about')
#@app.route('/contact')
#@app.route('/blog')
#def serve_static():
#    root_dir = os.path.dirname(os.getcwd())
#    return send_from_directory(os.path.join(root_dir, 'static'), 'course.html')
if __name__ == '__main__':
    app.run(debug=True)