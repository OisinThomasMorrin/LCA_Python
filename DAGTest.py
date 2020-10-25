import unittest
from DAG import *


class TestDAG(unittest.TestCase):

    # testing the set up of the constructor
    def test_v_less_than_zero(self):
        with self.assertRaises(ValueError):
            x = DAG(-1)

    # Test the indegree of a vertex in the graph
    def test_indegree(self):
        with self.assertRaises(ValueError):
            acyclic.indegree(-3)
        self.assertEqual(acyclic.indegree(5), 1)
        self.assertEqual(cycle.indegree(8), 2)

    # Test the outdegree of a vertex in the graph
    def test_outdegree(self):
        with self.assertRaises(ValueError):
            acyclic.outdegree(9)
        self.assertEqual(acyclic.outdegree(0), 1)
        self.assertEqual(cycle.outdegree(0), 2)

    # Test the adjacency array
    def test_adj(self):
        self.assertEqual(acyclic.adj(3), [4, 0, 0])
        self.assertEqual(cycle.adj(3), [1, 6, 0])

    # test the amount of edges with in a graph
    def test_E(self):
        self.assertEqual(acyclic.E, 7)
        self.assertEqual(cycle.E, 9)
        self.assertEqual(directedAyclic.E, 9)

    # test the number of vertices within a graph
    def test_V(self):
        self.assertEqual(acyclic.V, 8)
        self.assertEqual(cycle.V, 9)
        self.assertEqual(directedAyclic.V, 9)

    # test that the vertex passed through is valid for the graph (Non-negative)
    def test_add_edge(self):
        validTest = DAG(3)
        with self.assertRaises(ValueError):
            validTest.add_edge(-1, 2)
        with self.assertRaises(ValueError):
            validTest.add_edge(1, -2)
        with self.assertRaises(ValueError):
            validTest.add_edge(-1, -2)
        self.assertEqual(validTest.E, 0)
        validTest.add_edge(1, 2)
        self.assertEqual(validTest.E, 1)

    # test that the graph is acyclic, if there is a cycle the method will throw true that there is a cycle with in the graph
    def test_has_cycle(self):
        self.assertTrue(cycle.has_cycle())
        emptyGraph = DAG(0)
        self.assertFalse(emptyGraph.has_cycle())

    # Testing the LCA method
    def test_LCA(self):
        with self.assertRaises(ValueError):
            acyclic.find_LCA(2, 3)
        with self.assertRaises(ValueError):
            cycle.find_LCA(1, 4)
        with self.assertRaises(ValueError):
            directedAyclic.find_LCA(3, 4)
        with self.assertRaises(ValueError):
            directedAyclic.find_LCA(1, 4)
        with self.assertRaises(ValueError):
            directedAyclic.find_LCA(5, 2)
        with self.assertRaises(ValueError):
            directedAyclic.find_LCA(1, 5)
        with self.assertRaises(ValueError):
            directedAyclic.find_LCA(5, 1)
        with self.assertRaises(ValueError):
            acyclic.find_LCA(3, 3)
        with self.assertRaises(ValueError):
            emptyGraph = DAG(0)
            emptyGraph.find_LCA(2, 3)


if __name__ == '__main__':
    acyclic = DAG(8)
    acyclic.add_edge(0, 1)
    acyclic.add_edge(1, 2)
    acyclic.add_edge(2, 3)
    acyclic.add_edge(3, 4)
    acyclic.add_edge(4, 5)
    acyclic.add_edge(5, 6)
    acyclic.add_edge(6, 7)
    cycle = DAG(9)
    cycle.add_edge(0, 1)
    cycle.add_edge(0, 2)
    cycle.add_edge(1, 2)
    cycle.add_edge(2, 4)
    cycle.add_edge(4, 3)
    cycle.add_edge(3, 1)
    cycle.add_edge(3, 6)
    cycle.add_edge(6, 8)
    cycle.add_edge(7, 8)
    directedAyclic = DAG(9)
    directedAyclic.add_edge(0, 1)
    directedAyclic.add_edge(0, 2)
    directedAyclic.add_edge(1, 3)
    directedAyclic.add_edge(2, 4)
    directedAyclic.add_edge(3, 5)
    directedAyclic.add_edge(4, 6)
    directedAyclic.add_edge(5, 7)
    directedAyclic.add_edge(6, 7)
    directedAyclic.add_edge(7, 8)
    unittest.main()
