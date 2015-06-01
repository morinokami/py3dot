#!/usr/bin/env python3

# Example from http://www.graphviz.org/content/unix

from py3dot import Graph

unix = Graph({'size': '6, 6'})
unix.set_node_attr({'color': 'lightblue2', 'style': 'filled'})

unix.add_edge('5th Edition', '6th Edition')
unix.add_edge('5th Edition', 'PWB 1.0')
unix.add_edge('6th Edition', 'LSX')
unix.add_edge('6th Edition', '1 BSD')
unix.add_edge('6th Edition', 'Mini Unix')
unix.add_edge('6th Edition', 'Wollongong')
unix.add_edge('6th Edition', 'Interdata')
unix.add_edge('Interdata', 'Unix/TS 3.0')
unix.add_edge('Interdata', 'PWB 2.0')
unix.add_edge('Interdata', '7th Edition')
unix.add_edge('7th Edition', '8th Edition')
unix.add_edge('7th Edition', '32V')
unix.add_edge('7th Edition', 'V7M')
unix.add_edge('7th Edition', 'Ultrix-11')
unix.add_edge('7th Edition', 'Xenix')
unix.add_edge('7th Edition', 'UniPlus+')
unix.add_edge('V7M', 'Ultrix-11')
unix.add_edge('8th Edition', '9th Edition')
unix.add_edge('1 BSD', '2 BSD')
unix.add_edge('2 BSD', '2.8 BSD')
unix.add_edge('2.8 BSD', 'Ultrix-11')
unix.add_edge('2.8 BSD', '2.9 BSD')
unix.add_edge('32V', '3 BSD')
unix.add_edge('3 BSD', '4 BSD')
unix.add_edge('4 BSD', '4.1 BSD')
unix.add_edge('4.1 BSD', '4.2 BSD')
unix.add_edge('4.1 BSD', '2.8 BSD')
unix.add_edge('4.1 BSD', '8th Edition')
unix.add_edge('4.2 BSD', '4.3 BSD')
unix.add_edge('4.2 BSD', 'Ultrix-32')
unix.add_edge('PWB 1.0', 'PWB 1.2')
unix.add_edge('PWB 1.0', 'USG 1.0')
unix.add_edge('PWB 1.2', 'PWB 2.0')
unix.add_edge('USG 1.0', 'CB Unix 1')
unix.add_edge('USG 1.0', 'USG 2.0')
unix.add_edge('CB Unix 1', 'CB Unix 2')
unix.add_edge('CB Unix 2', 'CB Unix 3')
unix.add_edge('CB Unix 3', 'Unix/TS++')
unix.add_edge('CB Unix 3', 'PDP-11 Sys V')
unix.add_edge('USG 2.0', 'USG 3.0')
unix.add_edge('USG 3.0', 'Unix/TS 3.0')
unix.add_edge('PWB 2.0', 'Unix/TS 3.0')
unix.add_edge('Unix/TS 1.0', 'Unix/TS 3.0')
unix.add_edge('Unix/TS 3.0', 'TS 4.0')
unix.add_edge('Unix/TS++', 'TS 4.0')
unix.add_edge('CB Unix 3', 'TS 4.0')
unix.add_edge('TS 4.0', 'System V.0')
unix.add_edge('System V.0', 'System V.2')
unix.add_edge('System V.2', 'System V.3')

unix.save_fig('unix.png')
