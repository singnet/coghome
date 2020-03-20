from queue import Queue
from coghome.hass_communicator import start_HassCommunicator_in_thread
from coghome.home_state import HomeState
from coghome.event import Event
from coghome.entity import safe_load_entity_ids, safe_save_entity_ids
from opencog.type_constructors import *
from opencog.utilities import initialize_opencog
from opencog.bindlink import execute_atom
import configparser


class Launcher:
    def __init__(self, fname):
        self.config = configparser.ConfigParser()
        self.config.read(fname)

        self.__atomspace = AtomSpace()
        initialize_opencog(self.atomspace)

        self.queue_send = Queue()
        self.queue_recv = Queue()

        self.hass_thread = start_HassCommunicator_in_thread(
            self.config['DEFAULT']['uri'], self.config['DEFAULT']['token'],
            self.queue_send, self.queue_recv)

        self.home_state = HomeState(
            self.queue_recv.get(), self.queue_send,
            safe_load_entity_ids(self.config['DEFAULT']['known_entity_ids_file']))
        safe_save_entity_ids(self.home_state.get_all_entity_ids(),
                             self.config['DEFAULT']['known_entity_ids_file'])

        self.__current_event_gon = GroundedObjectNode("current_event", None)

    def process_event(self, msg):
        if (msg["type"] != "event"):
            return False
        if (msg["event"]["event_type"] == "state_changed"):
            self.home_state.state_changed_event_handler(msg["event"])
        self.current_event_gon.set_object(Event(msg["event"]))
        return True

    def stop(self):
        self.queue_send.put(None)
        self.hass_thread.join()
        
    def reactive_loop(self, reactive_bls):
        while(1):
            msg = self.queue_recv.get()
            if self.process_event(msg):
                for bl in reactive_bls:
                    execute_atom(self.atomspace, bl)

    @property
    def atomspace(self):
        return self.__atomspace

    @property
    def current_event_gon(self):
        return self.__current_event_gon
