from opencog.type_constructors import ConceptNode
from opencog.atomspace import types

class Entity:
    def __init__(self, state_dict, queue_send):
        self.set_state(state_dict)
        self.queue_send = queue_send
        
    def set_state(self, state_dict):
        self.entity_id = state_dict["entity_id"]
        self.state = state_dict["state"]
        self.attributes = state_dict["attributes"]
        self.last_changed = state_dict["last_changed"]
        self.last_updated = state_dict["last_updated"]
        
    def send_simple_command(self, service):
        service_data = { "entity_id": self.entity_id }
        msg = {"type": "call_service",  "domain": self.get_domain(), "service": service.name, "service_data": service_data}
        self.queue_send.put(msg)
    
    def send_command(self, service, data_atoms):
        service_data = { "entity_id": self.entity_id }
        if data_atoms.type == types.GroundedObjectNode:
            service_data.update(data_atoms.get_object())
        if data_atoms.type == types.ListLink:
            for a in data_atoms.out:
                if a.type == types.GroundedObjectNode:
                    service_data.update(a.get_object())
        msg = {"type": "call_service",  "domain": self.get_domain(), "service": service.name, "service_data": service_data}
        self.queue_send.put(msg)

    def get_state_cn(self):
        return ConceptNode(self.state)

    def get_domain(self):
        return self.entity_id.split(".")[0]

    
def entity_unavailable_state(entity_id):
    return {'entity_id': entity_id, 'state': 'unavailable', 'last_changed': '0000-00-00T00:00:00.000000+00:00', 'last_updated': '0000-00-00T00:00:00.000000+00:00', 'attributes' : {}}


def safe_load_entity_ids(fname):
    try:
        with open(fname) as f:
            content = f.readlines()
            content = [x.strip() for x in content] 
            return content
    except:
        return []
    
def safe_save_entity_ids(entity_ids, fname):
    try:
        with open(fname, 'w') as f:
            for e in entity_ids:
                f.write("%s\n"%e)
    except:
        pass
    
