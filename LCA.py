class Node:
    def __init__(self, key):
        self.key = key
        self.pred = []
        self.succ = []
  

def dagLCA(root,node_1,node_2):
    #base cases
    if root is None:
        return None
    elif node_1 is None or node_2 is None:
        return None
    elif root.key == node_1.key or root.key == node_2.key:
        return root.key
    elif node_1 == node_2:
        return node_1.key
    #perform lca computation 
    #Also note that this works for cyclic graphs as well.
    else:
        lca = []
        i=0

        while(i<len(node_1.pred)):
            j=0
            while(j<len(node_2.pred)):           
                if(node_1.pred[i].key == node_2.pred[j].key):
                    lca.append(node_1.pred[i].key)
                    j+=1
                else:
                    j+=1
            i+=1

        if(lca == []):
            if(node_1.key > node_2.key):
                lca.append(dagLCA(root,node_1.pred[0],node_2))
            else:
                lca.append(dagLCA(root,node_1,node_2.pred[0]))

        return lca
