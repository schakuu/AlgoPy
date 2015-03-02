print('Hello World')

from UndirectedGraph import UndirectedGraph
from Vertex import Vertex
from Edge import Edge

lines = [line.strip() for line in open("kargerMinCut.txt", 'r')]
graph = UndirectedGraph()

for l in lines:
    tokens = l.split()
    v1 = graph.addVertex(tokens[0])
    print(v1)
