class Graph:
  def __init__(self, nodes):
    self.nodes = nodes
    self.edges = []
  def add_edge(self, a, b):
    self.edges.append([a,b])
    
