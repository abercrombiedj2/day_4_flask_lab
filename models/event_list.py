from models.event import Event

event_1 = Event("Pool Tournament", "16/09/21", 16, "Next Door", "Cohort pool tournament. Who is the best?", True)
event_2 = Event("Karaoke", "17/09/21", 12, "Clockwise Building", "A terrible singing competition.", False)
event_3 = Event("Drink Beer", "23/09/21", 14, "Bier Halle", "Drinking lots and lots of beer.", True)

events = [event_1, event_2, event_3]

def add_new_event(event):
    events.append(event)

def remove_event(event):
    events.remove(event)
