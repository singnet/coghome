from opencog.type_constructors import *




def opencog_reactive_automation_bindlinks(gb_current_event):  
    
    bls = []
    bls.append(BindLink(AndLink(EvaluationLink(PredicateNode ("placed-in"), ListLink(VariableNode("button"), ConceptNode("room2"))),
                                EvaluationLink(PredicateNode ("placed-in"), ListLink(VariableNode("lamp"), ConceptNode("room1"))),
                                EvaluationLink(PredicateNode ("placed-in"), ListLink(VariableNode("door_sensor"), ConceptNode("front-door"))),
                                InheritanceLink(VariableNode("lamp"), ConceptNode("light")),
                                InheritanceLink(VariableNode("button1"), ConceptNode("button")),
                                InheritanceLink(VariableNode("door_sensor"), ConceptNode("door_windows_sensor")),
                                EqualLink(ApplyLink(MethodOfLink(gb_current_event, ConceptNode("get_type_cn")), ListLink()), ConceptNode("click")),
                                EvaluationLink(PredicateNode("has_id"),
                                               ListLink(VariableNode("button1"), ApplyLink(MethodOfLink(gb_current_event, ConceptNode("get_data_cn")), ListLink(ConceptNode("entity_id"))))),
                                EqualLink(ApplyLink(MethodOfLink(gb_current_event, ConceptNode("get_data_cn")), ListLink(ConceptNode("click_type"))), ConceptNode("single")),
                                EqualLink(ApplyLink(MethodOfLink(VariableNode("door_sensor"), ConceptNode("get_state_cn")), ListLink()), ConceptNode("off")),
                                EqualLink(ApplyLink(MethodOfLink(VariableNode("lamp"), ConceptNode("get_state_cn")), ListLink()), ConceptNode("off"))),
               ApplyLink(MethodOfLink(VariableNode("lamp"), ConceptNode("send_simple_command")), ListLink(ConceptNode("turn_on")))))

    bls.append(BindLink(AndLink(EvaluationLink(PredicateNode ("placed-in"), ListLink(VariableNode("button"), ConceptNode("room2"))),
                                EvaluationLink(PredicateNode ("placed-in"), ListLink(VariableNode("lamp"), ConceptNode("room1"))),
                                EvaluationLink(PredicateNode ("placed-in"), ListLink(VariableNode("door_sensor"), ConceptNode("front-door"))),
                                InheritanceLink(VariableNode("lamp"), ConceptNode("light")),
                                InheritanceLink(VariableNode("button1"), ConceptNode("button")),
                                InheritanceLink(VariableNode("door_sensor"), ConceptNode("door_windows_sensor")),
                                EqualLink(ApplyLink(MethodOfLink(gb_current_event, ConceptNode("get_type_cn")), ListLink()), ConceptNode("click")),
                                EvaluationLink(PredicateNode("has_id"),
                                               ListLink(VariableNode("button1"), ApplyLink(MethodOfLink(gb_current_event, ConceptNode("get_data_cn")), ListLink(ConceptNode("entity_id"))))),
                                EqualLink(ApplyLink(MethodOfLink(gb_current_event, ConceptNode("get_data_cn")), ListLink(ConceptNode("click_type"))), ConceptNode("double")),
                                EqualLink(ApplyLink(MethodOfLink(VariableNode("door_sensor"), ConceptNode("get_state_cn")), ListLink()), ConceptNode("off")),
                                EqualLink(ApplyLink(MethodOfLink(VariableNode("lamp"), ConceptNode("get_state_cn")), ListLink()), ConceptNode("on"))),
               ApplyLink(MethodOfLink(VariableNode("lamp"), ConceptNode("send_simple_command")), ListLink(ConceptNode("turn_off")))))               
    return bls
