import sys
from graph import Graph
import math
DEFAULT_NON_HAMILTON_SATURATION = 50
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
    try:
      nodes = int(get_input("nodes> "))
    except (ValueError) :
      print("Nodes must be an integer.")
      sys.exit(1)
    except(KeyboardInterrupt, EOFError):
      print("\nExiting...")
      sys.exit(1)
    if nodes<=10:
      print("Nodes count must be greater than 10")
      sys.exit(1)
    try:
      saturation = int(get_input("saturation> (0 - 100) "))
    except (ValueError):
      print("Saturation must be an integer")
      sys.exit(1)
    except(KeyboardInterrupt, EOFError):
      print("\nExiting...")
      sys.exit(1)
    if saturation < 0 or saturation > 100:
      print("Saturation must be between and 100")
      sys.exit(1)
    if saturation < 200/(nodes-1):
      print(f"Saturation is too low. For {nodes} nodes minimal saturation required to create a Hamiltonian cycle is {math.ceil(200/(nodes-1))}%")
      sys.exit(1)
    graph = Graph(nodes,saturation)
    graph.hamilton()

  elif action == "--non-hamilton":
    try:
      nodes = int(get_input("nodes> "))
    except (ValueError):
      print("Nodes counts must be an integer")
      sys.exit(1)
    except(KeyboardInterrupt, EOFError):
      print("\nExiting...")
      sys.exit(1)
    if nodes<=0:
      print("Nodes count must be greater than 0")
      sys.exit(1)
    graph = Graph(nodes, DEFAULT_NON_HAMILTON_SATURATION)
    graph.non_hamilton()
  else:
    print("Usage: python main.py --hamilton OR python main.py --non-hamilton")
    sys.exit(1)

  while True:
    try:
      action = get_input("action> ").strip().lower()
    except (EOFError, KeyboardInterrupt):
      break
    if action == "print":
      graph.print_graph()
    elif action == "euler":
      path = graph.find_euler_cycle()
      if path:
        print(f"Found euler cycle: {path}")
      else:
        print("Euler cycle not found")
    elif action == "hamilton":
      path = graph.find_hamiltonian_cycle()
      if path:
        print(f"Found hamiltonian cycle: {path}")
      else:
        print("Hamiltonian cycle not found")
    elif action == "help":
      print("""Available commands:
    print - print current graph
    euler - check if euler cycle exists in current graph
    hamilton - check if hamiltonian cycle exists in current graph
    help - show this message
    exit - exit program""")
    elif action in ["exit", "quit"]:
      break
    else:
      print(f"Unknown command: {action}. Use 'help' to see available commands")
      continue
  print("\nExiting...")


if __name__ == "__main__":
  main()