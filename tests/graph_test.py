import unittest
from pygraphviz3.graph import Graph, Node, Edge

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(size='1.2, 2.3', label='Graph')
        self.graph.add_nodes_from(['A', 'B', 'C'])
        self.graph.add_edges_from([('A', 'B'), ('B', 'C')])

    def test_getitem(self):
        self.assertEqual('1.2, 2.3', self.graph['size'])
        self.assertEqual('Graph', self.graph['label'])

    def test_setitem(self):
        self.graph['label'] = 'Internet Graph'
        self.assertEqual('Internet Graph', self.graph['label'])

    def test_num_nodes(self):
        self.assertEqual(3, self.graph.num_nodes())

    def test_num_edges(self):
        self.assertEqual(2, self.graph.num_edges())

    def test_add_node(self):
        self.graph.add_node('D')
        self.assertEqual(4, self.graph.num_nodes())
        self.graph.add_node('D')
        self.assertNotEqual(5, self.graph.num_edges())

    def test_add_edge(self):
        self.graph.add_edge('B', 'A')
        self.assertEqual(3, self.graph.num_edges())
        self.graph.add_edge('B', 'A')
        self.assertNotEqual(4, self.graph.num_edges())
        # self.graph.add_edge('A', 'a')

    def test_get_node(self):
        node = self.graph.get_node('B')
        self.assertEqual('B', str(node))
        #with self.assertRaises(KeyError):
            #node = self.graph.get_node('Z')

    def test_get_edge(self):
        pass
        #edge = self.graph.get_edge('B', 'C')
        #self.assertEqual('B -> C', str(edge))
        #with self.assertRaises(KeyError):
            #edge = self.graph.get_edge('Z', 'A')

    def test_set_attr(self):
        self.graph.set_attr(size='1.0, 2.3', label='Digraph')
        self.assertEqual('1.0, 2.3', self.graph['size'])
        self.assertEqual('Digraph', self.graph['label'])

    def test_set_node_attr(self):
        pass

    def test_set_edge_attr(self):
        pass




class TestNode(unittest.TestCase):
    def setUp(self):
        self.node = Node('A', shape='circle')

    def test_str(self):
        self.assertEqual('A', str(self.node))

    def test_eq(self):
        node1 = Node('A')
        node2 = Node('B')
        self.assertEqual(self.node, self.node)
        self.assertEqual(self.node, node1)
        self.assertNotEqual(self.node, node2)

    def test_getitem(self):
        self.assertEqual('circle', self.node['shape'])

    def test_setitem(self):
        self.node['shape'] = 'box'
        self.assertEqual('box', self.node['shape'])

    def test_get_attr_method(self):
        self.assertEqual({'shape': 'circle'}, self.node.get_attr())

    def test_set_attr_method(self):
        self.node.set_attr(shape='box')
        self.assertEqual('box', self.node['shape'])

class TestEdge(unittest.TestCase):
    def setUp(self):
        self.edge = Edge('A', 'B', label='foo')

    def test_str(self):
        self.assertEqual('A -> B', str(self.edge))

    def test_eq(self):
        edge1 = Edge('A', 'B')
        edge2 = Edge('B', 'C')
        self.assertEqual(self.edge, self.edge)
        self.assertEqual(edge1, self.edge)
        self.assertNotEqual(edge1, edge2)

    def test_getitem(self):
        self.assertEqual('foo', self.edge['label'])

    def test_setitem(self):
        self.edge['label'] = 'bar'
        self.assertEqual('bar', self.edge['label'])

    def test_get_attr_method(self):
        self.assertEqual({'label': 'foo'}, self.edge.get_attr())

    def test_set_attr_method(self):
        self.edge.set_attr(label='bar')
        self.assertEqual('bar', self.edge['label'])

    def test_get_tail(self):
        self.assertEqual('A', self.edge.get_tail())

    def test_get_head(self):
        self.assertEqual('B', self.edge.get_head())


if __name__ == '__main__':
    unittest.main()
