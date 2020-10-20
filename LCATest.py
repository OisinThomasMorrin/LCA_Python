import unittest
from LCA import Node
from LCA import findLCA
from LCA import findPath

class TestLCA(unittest.TestCase):

    def test_not_root_LCA(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertEqual(findLCA(root, 4, 5), 2)

    def test_root_LCA(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertEqual(findLCA(root, 4, 6), 1)

    def test_empty_binary_tree(self):
        root = None
        self.assertEqual(findLCA(root, 1,2), -1)
    
    def test_root_only_binary_tree(self):
        root = Node(1)
        self.assertEqual(findLCA(root,2,3),-1)
    
    def test_find_path_empty(self):
        root = None
        x = Node(0)
        self.assertEqual(findPath(root,[],x), False)
    
    def test_find_path_only_root(self):
        root = Node(1)
        x = Node(0)
        self.assertEqual(findPath(root,[],x), False)
    
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
