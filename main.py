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
    if nodes<=0:
      print("Nodes count must be greater than 0")
      sys.exit(1)
    saturation = int(get_input("saturation> (0 - 100) "))
    if saturation < 0 or saturation > 100:
      print("Saturation must be between 0 and 100")
      sys.exit(1)
    graph = Graph(nodes)

  elif action == "--non-hamilton":
    nodes = int(get_input("nodes> "))
    if nodes<=0:
      print("Nodes count must be greater than 0")
      sys.exit(1)
    graph = Graph(nodes)
  else:
    print("Usage: python main.py --hamilton OR python main.py --non-hamilton")
    sys.exit(1)

  while True:
    action = get_input("action> ").strip().lower()
    # TODO: Komendy menu
    if action == "print":
      print()
    if action == "euler":
      print()
    if action == "hamilton":
      print()
    elif action in ["exit", "quit"]:
      print("Exiting...")
      break


if __name__ == "__main__":
  main()