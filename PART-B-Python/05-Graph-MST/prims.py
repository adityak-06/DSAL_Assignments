class Graph:
    def __init__(self, v):
        self.V = v
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, x, y):
        parent[x] = y

    def kruskal(self):
        self.edges.sort()
        parent = [i for i in range(self.V)]
        result = []

        for w, u, v in self.edges:
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                result.append((u, v, w))
                self.union(parent, x, y)

        print("MST:")
        for u, v, w in result:
            print(u, "-", v, "=", w)

g = Graph(4)
g.add_edge(0,1,10)
g.add_edge(0,2,6)
g.add_edge(0,3,5)
g.add_edge(1,3,15)
g.add_edge(2,3,4)

g.kruskal()