import unittest
import LCA

class TestLCA(unittest.TestCase):

    #test base cases 
    def test_LCA_base_cases(self):
        root = LCA.Node(1)
        node_2 = LCA.Node(2)
        node_3 = LCA.Node(3)
        root.succ = [node_2]
        node_2.succ = [node_3]
        node_2.pred = [root]
        node_3.pred = [node_2]
        self.assertEqual(LCA.dagLCA(root, root, node_3), 1) #root and different key
        self.assertEqual(LCA.dagLCA(root, node_3, root), 1) #different key and root
        self.assertEqual(LCA.dagLCA(root, node_3, node_3), 3) #different key and root
        self.assertEqual(LCA.dagLCA(root, root, root), 1) #root and root
        self.assertEqual(LCA.dagLCA(root, None, root), None) #None and root
        self.assertEqual(LCA.dagLCA(root, root, None), None) #root and none
        self.assertEqual(LCA.dagLCA(None, root, node_3), None) #root is none
    
    #test cyclic - at the moment returns value of greatest node in cycle
    # slash with dot/apostrophe signifies direction of relation
    #      4
    #    ./ \.       
    # 1->2 ->3
    # '\____/'
    def test_cyclic(self):
        root = LCA.Node(1)
        node_2 = LCA.Node(2)
        node_3 = LCA.Node(3)
        node_4 = LCA.Node(4)
        root.succ = [node_2, node_3]
        root.pred = [node_3]
        node_2.succ = [node_3]
        node_2.pred = [root, node_4]
        node_3.succ = [root]
        node_3.pred = [node_2, node_4, root]
        node_4.succ = [node_2, node_3]
        self.assertEqual(LCA.dagLCA(root, node_2, node_3), [1,4])

    # strong connected (complete) k_4 graph - returns array of graph nodes less the two nodes to be checked
    def test_strongly_connected(self):
        root = LCA.Node(1)
        node_2 = LCA.Node(2)
        node_3 = LCA.Node(3)
        node_4 = LCA.Node(4)
        root.succ = [node_2, node_3,node_4]
        root.pred = [node_2, node_3,node_4]
        node_2.succ = [root, node_3, node_4]
        node_2.pred = [root, node_3, node_4]
        node_3.succ = [root, node_2, node_4]
        node_3.pred = [root, node_2, node_4]
        node_4.succ = [root, node_2, node_3]
        node_4.pred = [root, node_2, node_3]
        self.assertEqual(LCA.dagLCA(root, node_2, node_4), [1,3])



if __name__ == '__main__':
    unittest.main()
