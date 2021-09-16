from flask.helpers import send_file


class Event:
    def __init__(self, name, date, guests, location, description, weekly):
        self.name = name
        self.date = date
        self.guests = guests
        self.location = location
        self.description = description
        self.weekly = weekly