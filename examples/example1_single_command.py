from queue import Queue
import sys
sys.path.append('../')
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


GroundedObjectNode(":bright", {"brightness": 100})
GroundedObjectNode(":dim", {"brightness": 20})
GroundedObjectNode(":red", {"hs_color": [0, 100]})
GroundedObjectNode(":green", {"hs_color": [128, 100]})
GroundedObjectNode(":yellow", {"hs_color": [128, 100]})

a = BindLink(
        EvaluationLink(PredicateNode("has_domain"), ListLink(VariableNode("$l"), ConceptNode("light"))),
        ApplyLink(MethodOfLink(VariableNode("$l"), ConceptNode("send_command")),
              ListLink(ConceptNode("turn_on"),
                       ListLink(GroundedObjectNode(":dim"), GroundedObjectNode(":green")))))

execute_atom(atomspace, a)
l.stop()

