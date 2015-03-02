from Vertex import Vertex

class UndirectedGraph(object):
    """undirected graph"""
    def __init__(self):
        self.vertices = {}
        self.edges = {}

    def addVertex(self, name):
        if name not in self.vertices.keys():
            self.vertices[name] = Vertex(name)
        return self.vertices[name]
