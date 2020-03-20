from queue import Queue
from coghome.hass_communicator import start_HassCommunicator_in_thread
from coghome.home_state import HomeState
from coghome.event import Event
from coghome.entity import safe_load_entity_ids, safe_save_entity_ids
from coghome.launcher import Launcher
from opencog.type_constructors import *
from opencog.utilities import initialize_opencog
from opencog.bindlink import execute_atom
import configparser
from opencog_reactive_automation_bindlinks import opencog_reactive_automation_bindlinks
from knowledge_base import knowledge_base
from time import sleep



l = Launcher('config.cfg')
atomspace = l.atomspace

knowledge_base()
reactive_bls = opencog_reactive_automation_bindlinks(l.current_event_gon)
l.reactive_loop(reactive_bls)

