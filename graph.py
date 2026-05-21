import random
import itertools
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
    all_cycles = list(itertools.combinations(nodes_list,3))
    random.shuffle(all_cycles)
    for cycle in all_cycles:
      if self.current_edges_count + 3 > self.edges_to_create:
        break
      edges_list = self.check_if_edges_exist(cycle)
      if edges_list!=0:
        for node1,node2 in edges_list:
          self.add_edge(node1, node2)

      
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
    node_to_del = self.nodes
    new_edges = []
    deleted_count = 0
    nodes_list = [i for i in range (1,self.nodes+1)]
    for edge in self.edges:
        if edge[0] == node_to_del or edge[1] == node_to_del:
            deleted_count += 1
        else:
            new_edges.append(edge)
    self.edges = new_edges
    self.current_edges_count -= deleted_count
    nodes_list.remove(node_to_del)
    while self.current_edges_count <= self.edges_to_create:
      selected_nodes = random.sample(nodes_list,2)
      selected_nodes.sort()
      if tuple(selected_nodes) not in self.edges:
        self.add_edge(selected_nodes[0],selected_nodes[1])
    
  def print_graph(self):
    for start, destination in self.edges:
      print(f"{start} -> {destination}")
    print(f"Saturation: {self.saturation}")

  def get_adj_list(self):
    adj = {i: [] for i in range(1, self.nodes + 1)}
    for u,v in self.edges:
      adj[u].append(v)
      adj[v].append(u)
    return adj
  def find_hamiltonian_cycle(self):
    adj = self.get_adj_list()
    for v in adj.values():
      if len(v) < 2:
        return None
    path = [1]
    visited = {1}

    def visit(node):
      if len(path) == self.nodes:
        if 1 in adj[node]:
          path.append(1)
          return True
        return False
      for neighbor in adj[node]:
        if neighbor not in visited:
          visited.add(neighbor)
          path.append(neighbor)
          if visit(neighbor):
            return True
          visited.remove(neighbor)
          path.pop()
      return False

    if visit(1):
      return path
    else:
      return None
  def find_euler_cycle(self):
    adj = self.get_adj_list()
    for node, neighbors in adj.items():
      if len(neighbors) % 2 != 0:
        return None
    adj_copy = {u: list(v) for u,v in adj.items()}
    start_node = 1
    for node in adj_copy:
      if len(adj_copy[node]) > 0:
        start_node = node
        break
    stack = [start_node]
    path = []

    while stack:
      v = stack[-1]
      if adj_copy[v]:
        u = adj_copy[v].pop()
        adj_copy[u].remove(v)
        stack.append(u)
      else:
        path.append(stack.pop())

    if len(path) == len(self.edges) + 1:
      return path
    else:
      return None
