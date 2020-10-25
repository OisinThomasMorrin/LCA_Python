class DAG:
    def __init__(self, vertices):
        if vertices < 0:
            raise ValueError
        else:
            self.V = vertices
            self.E = 0
            self.indegreeArr = [0] * vertices
            self.outdegreeArr = [0] * vertices
            self.visited = [0] * vertices
            self.adjArr = [[0 for y in range(vertices)]
                        for x in range(vertices)]

    def validate_vertex(self, v):
        if v < 0 or v >= self.V:
            raise ValueError

    def add_edge(self, v, w):
        self.validate_vertex(v)
        self.validate_vertex(w)
        self.adjArr[v][w] = 1
        self.indegreeArr[w] += 1
        self.outdegreeArr[v] += 1
        self.E += 1

    def remove_edge(self, v, w):
        self.validate_vertex(v)
        self.validate_vertex(w)
        self.adjArr[v][w] = 0
        self.indegreeArr[w] -= 1
        self.outdegreeArr[v] -= 1
        self.E -= 1

    def outdegree(self, v):
        self.validate_vertex(v)
        return self.outdegreeArr[v]

    def indegree(self, v):
        self.validate_vertex(v)
        return self.indegreeArr[v]

    def adj(self, v):
        self.validate_vertex(v)
        temp = [0] * v
        count = 0
        for i in range(self.V):
            if self.adjArr[v][i] == 1:
                temp[count]=i
                count += 1
        return temp
    
    def has_cycle(self):
        count = 0
        for i in range(self.V):
            self.visited[count]=i
            for j in range(self.V):
                for k in range(self.V):
                    if self.visited[k] == j and self.adjArr[i][j] == 1:
                        return True
                        
            count += 1
        return False
    
    def find_LCA(self, v, w):
        self.validate_vertex(v)
        self.validate_vertex(w)
        self.has_cycle()
        if self.E > 0 and not self.has_cycle():
            return self.LCA_util(v,w)
        else:
            raise ValueError
    
    def LCA_util(self, v, w):
        vArr = [0] * self.E
        wArr = [0] * self.E
        vMarked = [False] * self.V
        wMarked = [False] * self.V
        vArr = [False] * self.V
        vCount = 0
        wCount = 0
        vArr[vCount] = v
        wArr[wCount] = w
        for i in range(self.V):
            vMarked[v] = True
            wMarked[w] = True
            for j in range(self.V):
                if self.adjArr[i][j] == 1 and vMarked[i]:
                    vCount += 1
                    vArr[vCount] = j
                    vMarked[j] = True
                if self.adjArr[i][j] == 1 and wMarked[i]:
                    wCount += 1
                    wArr[wCount] = j
                    wMarked[j] = True
                if wArr[wCount] == vArr[vCount]:
                    return wArr[wCount]
        return -1

