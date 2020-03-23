import sys, os
main_dir = os.path.split(os.path.abspath(__file__))[0]
sys.path.append(os.path.join(main_dir, ".."))

from coghome.launcher import Launcher
from opencog.type_constructors import *
from opencog.bindlink import execute_atom
import configparser
from time import sleep


l = Launcher(os.path.join(main_dir, 'config.cfg'))
atomspace = l.atomspace

# a convenient way to pass arguments to send_command
GroundedObjectNode(":bright", {"brightness": 100})
GroundedObjectNode(":dim", {"brightness": 20})
GroundedObjectNode(":red", {"hs_color": [0, 100]})
GroundedObjectNode(":green", {"hs_color": [128, 100]})
GroundedObjectNode(":yellow", {"hs_color": [64, 100]})


# send_command with arguments: turn on all devices in the domain 'light'
# setting their brightness and color attributes
turn_lights_on = BindLink(
        EvaluationLink(PredicateNode("has_domain"),
                       ListLink(VariableNode("$l"), ConceptNode("light"))),
        ApplyLink(MethodOfLink(VariableNode("$l"), ConceptNode("send_command")),
                  ListLink(ConceptNode("turn_on"),
                           ListLink(GroundedObjectNode(":bright"), GroundedObjectNode(":red")))))

execute_atom(atomspace, turn_lights_on)

sleep(2)

# send_simple_command without arguments: turn off all devices in the domain 'light'
turn_lights_off = BindLink(
        EvaluationLink(PredicateNode("has_domain"),
                       ListLink(VariableNode("$l"), ConceptNode("light"))),
        ApplyLink(MethodOfLink(VariableNode("$l"), ConceptNode("send_simple_command")),
                  ListLink(ConceptNode("turn_off"))))

execute_atom(atomspace, turn_lights_off)

l.stop()

