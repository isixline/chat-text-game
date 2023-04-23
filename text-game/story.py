class Event:
    def __init__(self, text):
        self.text = text

class Option:
    def __init__(self, text):
        self.text = text

class Story:
    def __init__(self, events=None, options=None):
        self.backGroud = ""
        self.events = events or []
        self.options = options or []

    def add_event(self, event):
        self.events.append(event)

    def get_event(self, event_index):
        return self.events[event_index]
    
    def get_current_event(self):
        return self.events[-1] if self.events else Event(self.backGroud)