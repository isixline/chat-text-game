class Event:
    def __init__(self, next, options):
        self.current = next or ""
        self.next = next or ""
        self.options = options or []
        self.choice = 0

class Option:
    def __init__(self, text):
        self.text = text

class Story:
    def __init__(self, backGroud):
        self.backGroud = backGroud or ""
        self.events = []

    def summary_current(self):
        if len(self.events) == 1:
            self.events[-1].current = self.backGroud
            return
        prv_event = self.events[-2]
        self.events[-1].current = (prv_event.current + prv_event.next + prv_event.options[prv_event.choice].text + '。').replace('你', '小明')

    def add_event(self, event):
        self.events.append(event)
        self.summary_current()

    def get_event(self, event_index):
        return self.events[event_index]
    
    def get_current_event(self):
        if len(self.events) == 0:
            return Event(self.backGroud, [])
        return self.events[-1]