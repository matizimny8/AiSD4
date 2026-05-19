import random
class Graph:
  def __init__(self, nodes, saturation):
    self.nodes = nodes
    self.edges = []
    self.saturation = saturation
    self.current_edges_count = 0
    self.edges_to_create = 0
    
  def add_edge(self, a, b):
    self.edges.append((min(a,b),max(a,b)))
    self.current_edges_count+=1
  
  def hamilton(self):
    nodes_list = [i for i in range (1,self.nodes+1)]
    random.shuffle(nodes_list)
    max_edges = (self.nodes * (self.nodes - 1))//2
    self.edges_to_create = int((self.saturation / 100.0) * max_edges)
    for i in range(len(nodes_list)-1):
      self.add_edge(nodes_list[i],nodes_list[i+1])
    self.add_edge(nodes_list[-1],nodes_list[0])
    while self.current_edges_count+3 <= self.edges_to_create:
      selected_nodes = random.sample(nodes_list,3)
      edges_list = self.check_if_edges_exist(selected_nodes)
      if edges_list != 0:
        for node1, node2 in edges_list:
          self.add_edge(node1,node2)

  def check_if_edges_exist(self, selected_nodes):
    edges_list = []
    for i in range(len(selected_nodes)-1):
      if (min(selected_nodes[i],selected_nodes[i+1]),max(selected_nodes[i],selected_nodes[i+1])) in self.edges:
        return 0
      else:
        edges_list.append([selected_nodes[i],selected_nodes[i+1]])
        continue
    if (min(selected_nodes[-1],selected_nodes[0]),max((selected_nodes[-1],selected_nodes[0]))) in self.edges:
      return 0
    else:
      edges_list.append([selected_nodes[-1],selected_nodes[0]])
      return edges_list
    
  def non_hamilton(self):
    self.hamilton()
    nodeToDel = self.nodes
    nowe_krawedzie = []
    deleted_count = 0
    nodes_list = [i for i in range (1,self.nodes+1)]
    for edge in self.edges:
        if edge[0] == nodeToDel or edge[1] == nodeToDel:
            deleted_count += 1
        else:
            nowe_krawedzie.append(edge)
    self.edges = nowe_krawedzie
    self.current_edges_count -= deleted_count
    while self.current_edges_count <= self.edges_to_create:
      selected_nodes = random.sample(nodes_list,2)
      selected_nodes.sort()
      if tuple(selected_nodes) not in self.edges:
        self.add_edge(selected_nodes[0],selected_nodes[1])
    
  def print_graph(self):
    for start, destination in self.edges:
      print(f"{start} -> {destination}")
    print(f"Saturation: {self.saturation}")