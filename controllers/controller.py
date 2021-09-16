from flask import render_template, request
from app import app
from models.event_list import events, add_new_event, remove_event
from models.event import Event

@app.route("/events")
def index():
    return render_template("index.html", title="My Events", events=events)

@app.route("/events", methods=["GET", "POST"])
def add_event():
    event_name = request.form["name"]
    event_date = request.form["date"]
    event_guests = request.form["guests"]
    event_location = request.form["location"]
    event_description = request.form["description"]
    event_weekly = request.form.get("weekly")
    new_event = Event(event_name, event_date, event_guests, event_location, event_description, event_weekly)
    add_new_event(new_event)
    return render_template("index.html", title="My Events", events=events)

@app.route('/events/delete/<index>', methods=['POST'])
def remove(index):
    event_to_remove = events[int(index)]
    remove_event(event_to_remove)
    return render_template('events.html', title='My Events', events=events)