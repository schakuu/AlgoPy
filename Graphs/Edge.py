class Edge(object):
    """a undirected edge"""
    def __init__(self, vertices):
        self.vertices = vertices
 
    def isSelfLoop(self):
        return vertices[0] == vertices[1]