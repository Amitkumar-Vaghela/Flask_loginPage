from flask import Flask , render_template
from flask_wtf import FlaskForm
from wtfforms import StringField ,PasswordField , SubmitField
from wtffrom.validator import DataRequired , Email , ValidationError

app =Flask(__name__)


@app.route('/')
def Home():
    return  render_template('home.html') 

@app.route('/login')
def Login():
    return  render_template('login.html') 

@app.route('/dashboard')
def dashboard():
    return  render_template('dashboard.html') 

@app.route('/register')
def register():
    return  render_template('register.html') 

if __name__ =='__main__':
    app.run(debug= True)
