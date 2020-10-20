import unittest
from LCA import Node
from LCA import findLCA
from LCA import findPath

class TestLCA(unittest.TestCase):

    #checks for LCA when LCA is a child of the root
    def test_not_root_LCA(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertEqual(findLCA(root, 4, 5), 2)

    #check LCA can be found that is the root if it is the LCA
    def test_root_LCA(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertEqual(findLCA(root, 4, 6), 1)

    #check empty binary tree cannot have a LCA
    def test_empty_binary_tree(self):
        root = None
        self.assertEqual(findLCA(root, 1,2), -1)
    
    #checks LCA of root node doesn't exist
    def test_root_only_binary_tree(self):
        root = Node(1)
        self.assertEqual(findLCA(root,2,3),-1)
    
    #check that empty root can't be connected to another node that is not its child
    def test_find_path_empty(self):
        root = None
        x = Node(0)
        self.assertEqual(findPath(root,[],x), False)
    
    #check that no path can be found between root and any child node (x is not connected)
    def test_find_path_only_root(self):
        root = Node(1)
        x = Node(0)
        self.assertEqual(findPath(root,[],x), False)
    
    #check that path can be found from node to another node (child)
    def test_check_for_k(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertEqual(findPath(root, [], 2), True)

if __name__ == '__main__':
    unittest.main()
