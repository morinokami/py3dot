# graph.py
#!/usr/bin/env python3

"""Python 3 interface for Graphviz"""

import subprocess
from attributes import ATTR, GRAPH_ATTR, NODE_ATTR, EDGE_ATTR

__all__ = ['Graph']

DOT_TEMPLATE = '''digraph {{
graph [{graph_attr}];
node [{node_attr}];
edge [{edge_attr}];

{attr_for_each_node}

{rel}
}}'''


class Graph:

    def __init__(self, attr={}):
        self.nodes = []
        self.edges = []
        self.attr = set_attr_helper(attr, {}, 'graph')
        self.node_attr = {}
        self.edge_attr = {}

    def __setitem__(self, key, value):
        self.attr[key] = value

    def __getitem__(self, key):
        return self.attr[key]

    def num_nodes(self):
        '''Return the number of nodes in the graph.'''
        return len(self.nodes)

    def num_edges(self):
        '''Return the number of edges in the graph.'''
        return len(self.edges)

    def print_nodes(self):
        '''Print nodes.'''
        print([str(n) for n in self.nodes])

    def print_edges(self):
        '''Print edges.'''
        print([str(e) for e in self.edges])

    def add_node(self, node_name, attr={}):
        '''Add a node to the graph.

        Args:
            node_name: A node's name.
            attr: A dictionary of attributes for the node.
        '''

        node = Node(node_name, attr)
        if node not in self.nodes:
            self.nodes.append(node)

    def add_nodes_from(self, nodes_list):
        '''Add nodes to the graph.

        Args:
            nodes_list: A list which consists of node names.
        '''
        for node_name in nodes_list:
            self.add_node(node_name)

    def add_edge(self, tail, head, attr={}):
        '''Add an edge to the graph.

        Args:
            tail: A tail node's name.
            head: A head node's name.
            attr: A dictionary of attributes for the edge.
        '''
        self.add_node(tail)
        self.add_node(head)
        edge = Edge(tail, head, attr)
        if edge not in self.edges:
            self.edges.append(edge)
        else:
            pass  # raise already exists error

    def add_edges_from(self, edges_list):
        '''Add edges to the graph.

        Args:
            edges_list: A list which consists of edges. The first item of each
                edge is a tail, and the second one is a head.
        '''
        for tail, head in edges_list:
            self.add_edge(tail, head)

    def get_node(self, node_name):
        '''Return a node specified by the argument.'''
        for node in self.nodes:
            if str(node) == node_name:
                return node
        raise KeyError

    def get_edge(self, tail, head):
        '''Return an edge specified by the argument.'''
        for edge in self.edges:
            if edge.get_tail() == tail and edge.get_head() == head:
                return edge
        raise KeyError

    def set_attr(self, attr):
        '''Set multiple attributes of the graph at a time.'''
        set_attr_helper(attr, self.attr, 'graph')

    def set_node_attr(self, attr):
        '''Set multiple attributes of nodes at a time.'''
        set_attr_helper(attr, self.node_attr, 'node')

    def set_attr_for_nodes(self, nodes, attr):
        '''Set multiple attribues of some nodes at a time.'''
        for node_name in nodes:
            node = self.get_node(node_name)
            node.set_attr(attr)

    def set_edge_attr(self, attr):
        '''Set multiple attributes of edges at a time.'''
        set_attr_helper(attr, self.edge_attr, 'edge')

    def get_attr(self):
        '''Return attributes of the graph.'''
        return self.attr

    def get_node_attr(self):
        '''Return attributes of nodes.'''
        return self.node_attr

    def get_edge_attr(self):
        '''Return attributes of edges.'''
        return self.edge_attr

    def create_dot(self):
        '''Create a dot file.'''

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
        attr_for_each_node = ''
        for node in self.nodes:
            attr_str = get_attr_str(node.get_attr(), NODE_ATTR)
            attr_for_each_node += '"' + str(node) + '" [' + attr_str + '];\n'
        rel = ''
        for edge in self.edges:
            tail = edge.get_tail()
            head = edge.get_head()
            attr_str = get_attr_str(edge.get_attr(), EDGE_ATTR)
            rel += '"' + tail + '" -> "' + head + '" [' + attr_str + '];\n'

        return DOT_TEMPLATE.format(graph_attr=graph_attr, node_attr=node_attr,
                               edge_attr=edge_attr, attr_for_each_node=attr_for_each_node[:-1],
                               rel=rel[:-1])

    def save_fig(self, path):
        dot = self.create_dot().encode()
        p = subprocess.Popen(['dot', '-T', 'png', '-o', path], stdin=subprocess.PIPE)
        p.stdin.write(dot)
        output = p.communicate()[0]
        p.stdin.close()


class Node:

    def __init__(self, node_name, attr={}):
        self.name = node_name
        self.attr = set_attr_helper(attr, {}, 'node')

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __setitem__(self, key, value):
        self.attr[key] = value

    def __getitem__(self, key):
        return self.attr[key]

    def set_attr(self, attr):
        '''Set multiple attributes at a time.'''
        set_attr_helper(attr, self.attr, 'node')

    def get_attr(self):
        '''Return attributes of the node.'''
        return self.attr


class Edge:

    def __init__(self, tail, head, attr={}):
        self.tail = tail
        self.head = head
        self.attr = set_attr_helper(attr, {}, 'edge')
        self.attr = attr

    def __str__(self):
        return self.tail + ' -> ' + self.head

    def __eq__(self, other):
        return self.tail == other.tail and self.head == other.head

    def __setitem__(self, key, value):
        self.attr[key] = value

    def __getitem__(self, key):
        return self.attr[key]

    def set_attr(self, attr):
        '''Set multiple attributes at a time.'''
        set_attr_helper(attr, self.attr, 'edge')

    def get_attr(self):
        '''Return attributes of the edge.'''
        return self.attr

    def get_tail(self):
        '''Return the tail node of the edge as a string.'''
        return self.tail

    def get_head(self):
        '''Return the head node of the edge as a string.'''
        return self.head


def set_attr_helper(attr, target, kind):
    if kind == 'graph':
        ref = GRAPH_ATTR
    elif kind == 'node':
        ref = NODE_ATTR
    elif kind == 'edge':
        ref = EDGE_ATTR

    for attr_name in attr:
        if attr_name in ref:
            target[attr_name] = attr[attr_name]
        else:
            raise AttributeError

    return target


if __name__ == '__main__':

    graph = Graph({'size': '3.6, 6.9', 'label': 'Graph', 'labelloc': 't', 'fontsize': 10})
    graph.add_nodes_from(['A', 'B', 'C', 'D'])
    graph.add_edge('A', 'B', {'arrowhead':'dot'})
    graph.add_edge('A', 'C', {'arrowtail': 'odot'})
    graph.add_edge('A', 'D', {'headlabel': 'end', 'taillabel': 'start', 'labeldistance': 3, 'labelangle': 30})
    graph.add_edge('B', 'D')
    print(graph.create_dot())
    #graph.save_fig('sample2.svg')
