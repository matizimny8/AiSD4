import sys
from graph import Graph

def get_input(prompt):
  if sys.stdin.isatty():
    return input(prompt)
  else:
    return input()
  
def main():
  if len(sys.argv) < 2:
    print("Usage: python main.py --hamilton OR python main.py --non-hamilton")
    sys.exit(1)
  action = sys.argv[1]
  graph = None
  if action == "--hamilton":
    nodes = int(get_input("nodes> "))
    if nodes<=10:
      print("Nodes count must be greater than 10")
      sys.exit(1)
    saturation = int(get_input("saturation> (0 - 100) "))
    if saturation < 0 or saturation > 100:
      print("Saturation must be between 0 and 100")
      sys.exit(1)
    graph = Graph(nodes,saturation)
    graph.hamilton()

  elif action == "--non-hamilton":
    nodes = int(get_input("nodes> "))
    if nodes<=0:
      print("Nodes count must be greater than 0")
      sys.exit(1)
    graph = Graph(nodes,50)
    graph.non_hamilton()
  else:
    print("Usage: python main.py --hamilton OR python main.py --non-hamilton")
    sys.exit(1)

  while True:
    action = get_input("action> ").strip().lower()
    # TODO: Komendy menu
    if action == "print":
      graph.print_graph()
    elif action == "euler":
      print()
    elif action == "hamilton":
      path = graph.find_hamiltonian_cycle()
      if path:
        print(f"Found hamiltonian cycle: {path}")
      else:
        print("Hamiltonian cycle not found")
    elif action in ["exit", "quit"]:
      print("Exiting...")
      break


if __name__ == "__main__":
  main()