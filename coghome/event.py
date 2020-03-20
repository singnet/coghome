from opencog.type_constructors import ConceptNode

class Event:
    def __init__(self, event):
        assert "event_type" in event and "data" in event, "Wrong event structure" 
        self.event_type = event["event_type"].split(".")[-1]
        self.data = event["data"]

    def get_type_cn(self):
        return ConceptNode(self.event_type)
    
    def get_data_cn(self, key):
        return ConceptNode(self.data[key.name] if key.name in self.data else "None")

