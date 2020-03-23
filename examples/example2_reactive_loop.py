import sys, os
main_dir = os.path.split(os.path.abspath(__file__))[0]
sys.path.append(os.path.join(main_dir, ".."))

from coghome.launcher import Launcher
from opencog.type_constructors import *
from opencog.bindlink import execute_atom
import configparser
from time import sleep

# a helper function to make general rules for turning the lights on and turn_lights_off
# depending on the click type
def make_rule(click_type, command):
    return BindLink(
        AndLink(
            # $l is a lamp, and $b is a button
            InheritanceLink(VariableNode("$l"), ConceptNode("lamp")),
            InheritanceLink(VariableNode("$b"), ConceptNode("button")),
            # $l and $b are placed in the same $room
            EvaluationLink(
                PredicateNode("placed-in"),
                ListLink(VariableNode("$b"), VariableNode("$room"))),
            EvaluationLink(
                PredicateNode("placed-in"),
                ListLink(VariableNode("$l"), VariableNode("$room"))),
            # Entity $b has same id as indicated in the event
            EvaluationLink(
                PredicateNode("has_id"),
                ListLink(VariableNode("$b"),
                        ApplyLink(MethodOfLink(GroundedObjectNode("current_event"), ConceptNode("get_data_cn")),
                                ListLink(ConceptNode("entity_id"))))),
            # Check click_type
            EqualLink(
                ApplyLink(
                    MethodOfLink(
                        GroundedObjectNode("current_event"),
                        ConceptNode("get_data_cn")),
                    ListLink(ConceptNode("click_type"))),
                ConceptNode(click_type))),
        ApplyLink(MethodOfLink(VariableNode("$l"), ConceptNode("send_simple_command")),
                  ListLink(ConceptNode(command))))


l = Launcher(os.path.join(main_dir, 'config.cfg'))
atomspace = l.atomspace


# some knowledge about locations of the devices
# (use IDs of your own devices)
lamp = GroundedObjectNode("light.experiment_lamp_1")
button = GroundedObjectNode("binary_sensor.switch_158d00039928d1")
EvaluationLink(PredicateNode("placed-in"),
               ListLink(lamp, ConceptNode("bedroom")))
EvaluationLink(PredicateNode("placed-in"),
               ListLink(button, ConceptNode("bedroom")))
# declarative knowledge of the device types
InheritanceLink(lamp, ConceptNode("lamp"))
InheritanceLink(button, ConceptNode("button"))

# creating reactive control rules
bls = []
bls.append(make_rule("single", "turn_on"))
bls.append(make_rule("double", "turn_off"))

l.reactive_loop(bls)
