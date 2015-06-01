# graph.py
#!/usr/bin/env python3

"""Python 3 interface for Graphviz"""

import subprocess

from attributes import ATTR, GRAPH_ATTR, NODE_ATTR, EDGE_ATTR


class Graph:

    def __init__(self, *, size=None, label=None, labelloc=None,
                 fontname=None, fontsize=None, fontcolor=None, bgcolor=None,
                 rotate=None, rankdir=None):
        self.nodes = []
        self.edges = []
        self.attr = {
            'size': size,
            'label': label,
            'labelloc': labelloc,
            'fontname': fontname,
            'fontsize': fontsize,
            'fontcolor': fontcolor,
            'bgcolor': bgcolor,
            'rotate': rotate,
            'rankdir': rankdir
        }
        self.node_attr = {}
        self.edge_attr = {}

    def __setitem__(self, key, value):
        self.attr[key] = value

    def __getitem__(self, key):
        return self.attr[key]

    def num_nodes(self):
        '''Returns the number of nodes in the graph.'''
        return len(self.nodes)

    def num_edges(self):
        '''Returns the number of edges in the graph.'''
        return len(self.edges)

    def print_nodes(self):
        '''Print nodes.'''
        #for n in self.nodes

    def print_edges(self):
        '''Print edges.'''

    def add_node(self, node_name, shape=None):
        '''Add a node to the graph.

        Args:
            node_name: A node's name.
            attr:
        '''

        node = Node(node_name, shape=shape)
        if node not in self.nodes:
            self.nodes.append(node)

    def add_nodes_from(self, nodes_list):
        '''Add nodes to the graph.

        Args:
            nodes_list: A list which consists of node names.
        '''
        for node_name in nodes_list:
            self.add_node(node_name)

    def add_edge(self, tail, head, *, label=None, fontcolor=None,
                 labelfloat=None, headlabel=None, taillabel=None,
                 labeldistance=None, labelangle=None, color=None,
                 style=None, dir=None, arrowhead=None, arrowtail=None,
                 arrowsize=None):
        '''Add an edge to the graph.

        Args:
            tail: A tail node's name.
            head: A head node's name.
            attr:
        '''
        edge = Edge(tail, head, label=label, fontcolor=fontcolor,
                    labelfloat=labelfloat, headlabel=headlabel, taillabel=taillabel,
                    labeldistance=labeldistance, labelangle=labelangle, color=color,
                    style=style, dir=dir, arrowhead=arrowhead, arrowtail=arrowtail,
                    arrowsize=arrowsize)
        if edge not in self.edges:
            self.edges.append(edge)

    def add_edges_from(self, edges_list):
        '''Add edges to the graph.

        Args:
            edges_list: A list which consists of edges. The first item of each
                edge is a tail, and the second one is a head.
        '''
        for tail, head in edges_list:
            self.add_edge(tail, head)

    def get_node(self, node_name):
        '''Returns a node specified by the argument'''
        for node in self.nodes:
            if str(node) == node_name:
                return node
            else:
                raise KeyError

    def get_edge(self, tail, head):
        '''Returns an edge specified by the argument'''
        for edge in self.edges:
            if edge.get_tail() == tail and edge.get_head() == head:
                return edge
            else:
                raise KeyError

    def set_attr(self, *, size=None, label=None):
        '''Set multiple attributes at a time.'''
        self.attr['size'] = size
        self.attr['label'] = label

    def set_node_attr(self, shape):
        '''Set multiple attributes of nodes at a time.'''
        self.node_attr['shape'] = shape

    def set_edge_attr(self, label):
        '''Set multiple attributes of edges at a time.'''
        self.edge_attr['label'] = label

    def create_dot(self):
        '''Create a dot file.'''
        template = '''digraph {{
graph [{graph_attr}];
node [{node_attr}];
edge [{edge_attr}];
{attr_for_each_node}

{rel}
}}
'''

        def get_attr_str(attr, target):
            attr_str = []
            for attr_name in target:
                if attr_name in attr and attr[attr_name] is not None:
                    if ATTR[attr_name]['is_string']:
                        attr_str.append(attr_name + '="' +
                                         str(attr[attr_name]) + '"')
                    else:
                        attr_str.append(attr_name + '=' + str(attr[attr_name]))
            return ','.join(attr_str)

        graph_attr = get_attr_str(self.attr, GRAPH_ATTR)
        node_attr = get_attr_str(self.node_attr, NODE_ATTR)
        edge_attr = get_attr_str(self.edge_attr, EDGE_ATTR)
        rel = ''
        for edge in self.edges:
            tail = edge.get_tail()
            head = edge.get_head()
            attr_str = get_attr_str(edge.get_attr(), EDGE_ATTR)
            rel += tail + ' -> ' + head + '[' + attr_str + '];\n'

        return template.format(graph_attr=graph_attr, node_attr=node_attr,
                               edge_attr=edge_attr, attr_for_each_node='',
                               rel=rel)

    def save_fig(self, path):
        dot = self.create_dot().encode()
        p = subprocess.Popen(['dot', '-T', 'png', '-o', path], stdin=subprocess.PIPE)
        p.stdin.write(dot)
        output = p.communicate()[0]
        p.stdin.close()


class Node:

    def __init__(self, node_name, *, shape=None):
        self.name = node_name
        self.attr = {'shape': shape}
        '''
        self.shape
        self.size
        self.style
        self.peripheries
        self.color
        self.fillcolor
        self.label
        self.font*'''

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __setitem__(self, key, value):
        self.attr[key] = value

    def __getitem__(self, key):
        return self.attr[key]

    def set_attr(self, *, shape=None):
        '''Set multiple attributes at a time.'''
        self.attr['shape'] = shape

    def get_attr(self):
        '''Return all'''
        return self.attr


class Edge:

    def __init__(self, tail, head, *, label=None, fontcolor=None,
                 labelfloat=None, headlabel=None, taillabel=None,
                 labeldistance=None, labelangle=None, color=None,
                 style=None, dir=None, arrowhead=None, arrowtail=None,
                 arrowsize=None):

        self.tail = tail
        self.head = head
        self.attr = {
            'label': label,
            'fontcolor': fontcolor,
            'labelfloat': labelfloat,
            'headlabel': headlabel,
            'taillabel': taillabel,
            'labeldistance': labeldistance,
            'labelangle': labelangle,
            'color': color,
            'style': style,
            'dir': dir,
            'arrowhead': arrowhead,
            'arrowtail': arrowtail,
            'arrowsize': arrowsize
        }

    def __str__(self):
        return self.tail + ' -> ' + self.head

    def __eq__(self, other):
        return self.tail == other.tail and self.head == other.head

    def __setitem__(self, key, value):
        self.attr[key] = value

    def __getitem__(self, key):
        return self.attr[key]

    def set_attr(self, *, label=None):
        '''Set multiple attributes at a time.'''
        self.attr['label'] = label

    def get_attr(self):
        return self.attr

    def get_tail(self):
        return self.tail

    def get_head(self):
        return self.head


if __name__ == '__main__':
    graph = Graph(size='3.6, 6.9', label='Graph', labelloc='t', fontsize=10)
    graph.add_nodes_from(['A', 'B', 'C', 'D'])
    graph.add_edge('A', 'B', arrowhead='dot')
    graph.add_edge('A', 'C', arrowtail='odot')
    graph.add_edge('A', 'D', headlabel='end', taillabel='start', labeldistance=3, labelangle=30)
    graph.add_edge('B', 'D')
    graph.save_fig('sample2.png')
