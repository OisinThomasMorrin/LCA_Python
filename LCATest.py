import unittest
import LCA

class TestLCA(unittest.TestCase):

    #test base cases for 
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

if __name__ == '__main__':
    unittest.main()
