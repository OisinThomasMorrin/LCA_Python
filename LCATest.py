import unittest
from LCA import Node
from LCA import findLCA


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


if __name__ == '__main__':
    unittest.main()
