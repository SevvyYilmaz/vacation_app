from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import trip


#import the trip as well 
@app.route('/trips/dashboard')
def trips_dashboard():
    trips =trip.Trip.get_all_trips()
    return render_template("trips_dashboard.html", all_trips = trips)