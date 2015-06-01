import unittest
from py3dot.graph import Graph, Node, Edge


class GraphTest(unittest.TestCase):

    def test_getitem(self):
        graph = Graph({'size': '1.2, 2.3', 'label': 'Graph'})
        self.assertEqual('1.2, 2.3', graph['size'])
        self.assertEqual('Graph', graph['label'])

    def test_setitem(self):
        graph = Graph({'size': '1.2, 2.3', 'label': 'Graph'})
        graph['label'] = 'Internet Graph'
        self.assertEqual('Internet Graph', graph['label'])

    def test_num_nodes(self):
        graph = Graph()
        graph.add_nodes_from(['A', 'B', 'C'])
        self.assertEqual(3, graph.num_nodes())

    def test_num_edges(self):
        graph = Graph()
        graph.add_edges_from([('A', 'B'), ('B', 'C')])
        self.assertEqual(2, graph.num_edges())

    def test_add_node(self):
        graph = Graph()
        graph.add_nodes_from(['A', 'B', 'C'])
        graph.add_node('D')
        self.assertEqual(4, graph.num_nodes())
        graph.add_node('D')
        self.assertNotEqual(5, graph.num_edges())

    def test_add_edge(self):
        graph = Graph()
        graph.add_edges_from([('A', 'B'), ('B', 'C')])
        graph.add_edge('B', 'A')
        self.assertEqual(3, graph.num_edges())
        graph.add_edge('B', 'A')
        self.assertNotEqual(4, graph.num_edges())
        graph.add_edge('A', 'D')
        self.assertEqual(4, graph.num_edges())
        self.assertEqual(4, graph.num_nodes())

    def test_get_node(self):
        graph = Graph()
        graph.add_nodes_from(['A', 'B', 'C'])
        node = graph.get_node('B')
        self.assertEqual('B', str(node))
        with self.assertRaises(KeyError):
            node = graph.get_node('Z')

    def test_get_edge(self):
        graph = Graph()
        graph.add_edges_from([('A', 'B'), ('B', 'C')])
        edge = graph.get_edge('B', 'C')
        self.assertEqual('B -> C', str(edge))
        with self.assertRaises(KeyError):
            edge = graph.get_edge('Z', 'A')

    def test_set_attr(self):
        graph = Graph()
        graph.set_attr({'size': '1.0, 2.3', 'label': 'Digraph'})
        self.assertEqual('1.0, 2.3', graph['size'])
        self.assertEqual('Digraph', graph['label'])
        graph.set_attr({'rankdir': 'LR'})
        self.assertEqual('LR', graph['rankdir'])
        self.assertEqual({'size': '1.0, 2.3', 'label': 'Digraph',
                          'rankdir': 'LR'}, graph.get_attr())
        with self.assertRaises(AttributeError):
            graph.set_attr({'not_exists': 'foo'})

    def test_set_node_attr(self):
        pass

    def test_set_attr_for_nodes(self):
        pass

    def test_set_edge_attr(self):
        pass

    def test_get_attr(self):
        graph = Graph({'size': '1.0, 2.3', 'label': 'Digraph'})
        self.assertEqual({'size': '1.0, 2.3', 'label': 'Digraph'},
                         graph.get_attr())

    def test_get_node_attr(self):
        graph = Graph()
        graph.set_node_attr({'shape': 'circle'})
        self.assertEqual({'shape': 'circle'}, graph.get_node_attr())

    def test_get_edge_attr(self):
        graph = Graph()
        graph.set_edge_attr({'label': 'foo'})
        self.assertEqual({'label': 'foo'}, graph.get_edge_attr())

    def test_create_dot(self):
        graph = Graph({'size': '3.6, 6.9', 'label': 'Graph', 'labelloc': 't',
                       'fontsize': 10})
        graph.add_nodes_from(['A', 'B', 'C', 'D'])
        graph.add_edge('A', 'B', {'arrowhead': 'dot'})
        graph.add_edge('A', 'C', {'arrowtail': 'odot'})
        graph.add_edge('A', 'D', {'headlabel': 'end', 'taillabel': 'start',
                       'labeldistance': 3, 'labelangle': 30})
        graph.add_edge('B', 'D')
        expected = '''digraph {
graph [fontsize="10",label="Graph",labelloc="t",size="3.6, 6.9"];
node [];
edge [];

"A" [];
"B" [];
"C" [];
"D" [];

"A" -> "B" [arrowhead="dot"];
"A" -> "C" [arrowtail="odot"];
"A" -> "D" [headlabel="end",labelangle="30",labeldistance="3",taillabel="start"];
"B" -> "D" [];
}'''
        self.assertEqual(expected, graph.create_dot())


class TestNode(unittest.TestCase):

    def test_str(self):
        node = Node('A', {'shape': 'circle'})
        self.assertEqual('A', str(node))

    def test_eq(self):
        node0 = Node('A', {'shape': 'circle'})
        node1 = Node('A')
        node2 = Node('B')
        self.assertEqual(node0, node0)
        self.assertEqual(node0, node1)
        self.assertNotEqual(node0, node2)

    def test_getitem(self):
        node = Node('A', {'shape': 'circle'})
        self.assertEqual('circle', node['shape'])

    def test_setitem(self):
        node = Node('A', {'shape': 'circle'})
        node['shape'] = 'box'
        self.assertEqual('box', node['shape'])

    def test_get_attr(self):
        node = Node('A', {'shape': 'circle'})
        self.assertEqual({'shape': 'circle'}, node.get_attr())

    def test_set_attr(self):
        node = Node('A', {'shape': 'circle'})
        node.set_attr({'shape': 'box'})
        self.assertEqual('box', node['shape'])


class TestEdge(unittest.TestCase):

    def test_str(self):
        edge = Edge('A', 'B', {'label': 'foo'})
        self.assertEqual('A -> B', str(edge))

    def test_eq(self):
        edge0 = Edge('A', 'B', {'label': 'foo'})
        edge1 = Edge('A', 'B')
        edge2 = Edge('B', 'C')
        self.assertEqual(edge0, edge0)
        self.assertEqual(edge1, edge0)
        self.assertNotEqual(edge1, edge2)

    def test_getitem(self):
        edge = Edge('A', 'B', {'label': 'foo'})
        self.assertEqual('foo', edge['label'])

    def test_setitem(self):
        edge = Edge('A', 'B', {'label': 'foo'})
        edge['label'] = 'bar'
        self.assertEqual('bar', edge['label'])

    def test_get_attr(self):
        edge = Edge('A', 'B', {'label': 'foo'})
        self.assertEqual({'label': 'foo'}, edge.get_attr())

    def test_set_attr(self):
        edge = Edge('A', 'B', {'label': 'foo'})
        edge.set_attr({'label': 'bar'})
        self.assertEqual('bar', edge['label'])

    def test_get_tail(self):
        edge = Edge('A', 'B', {'label': 'foo'})
        self.assertEqual('A', edge.get_tail())

    def test_get_head(self):
        edge = Edge('A', 'B', {'label': 'foo'})
        self.assertEqual('B', edge.get_head())


if __name__ == '__main__':
    unittest.main()
