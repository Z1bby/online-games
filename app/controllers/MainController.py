from flask import render_template

def index():
    return render_template('index.html')

def login():
    return render_template('login.html')
