from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user

@app.route('/')
def index():
    return redirect('/users/dashboard')

@app.route('/users/dashboard')
def user_dashboard():
    users = user.User.get_all_users()
    print(users) # list objects will appear in terminal 
    return render_template("user_dashboard.html", all_users = users)