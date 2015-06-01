#!/usr/bin/env python3

fsm = Graph({'rankdir': 'LR', 'size': '8, 5'})
fsm.set_node_attr({'shape': 'circle'})
fsm.add_nodes_from(['LR_' + str(i) for i in range(9)])
fsm.set_attr_for_each_node(['LR_0', 'LR_3', 'LR_4', 'LR_8'], {'shape': 'doublecircle'})

fsm.add_edge('LR_0', 'LR_2', {'label': 'SS(B)'})
fsm.add_edge('LR_0', 'LR_1', {'label': 'SS(S)'})
fsm.add_edge('LR_1', 'LR_3', {'label': 'S($end)'})
fsm.add_edge('LR_2', 'LR_6', {'label': 'SS(b)'})
fsm.add_edge('LR_2', 'LR_5', {'label': 'SS(a)'})
fsm.add_edge('LR_2', 'LR_4', {'label': 'S(A)'})
fsm.add_edge('LR_5', 'LR_7', {'label': 'S(b)'})
fsm.add_edge('LR_5', 'LR_5', {'label': 'S(a)'})
fsm.add_edge('LR_6', 'LR_6', {'label': 'S(b)'})
fsm.add_edge('LR_6', 'LR_5', {'label': 'S(a)'})
fsm.add_edge('LR_7', 'LR_8', {'label': 'S(b)'})
fsm.add_edge('LR_7', 'LR_5', {'label': 'S(a)'})
fsm.add_edge('LR_8', 'LR_6', {'label': 'S(b)'})
fsm.add_edge('LR_8', 'LR_5', {'label': 'S(a)'})

fsm.save_fig('fsm.png')
