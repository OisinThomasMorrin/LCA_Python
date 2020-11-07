class Node:
    def __init__(self, key):
        self.key = key
        self.pred = []
        self.succ = []
  

def dagLCA(root,node_1,node_2):

    if root is None:
        return None
    elif root.key == node_1 or root.key == node_2:
        return root
    elif node_1 == node_2:
        return node_1.key
