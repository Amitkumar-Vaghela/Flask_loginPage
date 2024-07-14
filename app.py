from flask import Flask , render_template
from flask_wtf import FlaskForm
from wtfforms import StringField ,PasswordField , SubmitField
from wtffrom.validator import DataRequired , Email , VAlidationError

app =Flask(__name__)

class RegisterForm(FlaskForm):
    name = StringField (name, validator=[DataRequired()])
    email = StringField (Email, validator=[DataRequired() , Email()])
    password = StringField (Password, validator=[DataRequired()])
    submit =  SubmitField (Register)

@app.route('/')
def Home():
    return  render_template('home.html') 

@app.route('/register')
def register():
    return  render_template('register.html') 

@app.route('/login')
def login():
    return  render_template('login.html') 

@app.route('/dashboard')
def dashboard():
    return  render_template('dashboard.html') 

if __name__ =='__main__':
    app.run(debug= True)