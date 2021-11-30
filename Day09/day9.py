import networkx as nx
from typing import List, Optional, Set


def read_file() -> List[str]:
  with open('Day09/data.txt') as f:
    return [line.strip() for line in f.readlines()]

def walk(best_cost_fn, G : nx.Graph, currentNode: str, visited: Set[str]) -> Optional[int]:
  if len(visited) == len(G.nodes()):
    # We have completed a route
    return 0
  
  available_routes = G.edges(currentNode, data = True)
  if len(available_routes) == 0:
    # There is no route to the end
    return None

  best_cost_so_far = None  
  for (city_a, city_b, data) in available_routes:
    if city_b not in visited:
      visited.add(city_b)
      cost = walk(best_cost_fn, G, city_b, visited)
      if cost is not None:
        best_cost_so_far = data["cost"]+cost if best_cost_so_far is None else best_cost_fn(data["cost"]+cost, best_cost_so_far)      
      visited.remove(city_b)
  return best_cost_so_far

def solve(best_cost_fn):
  G = nx.Graph()
  lines = read_file()
  for line in lines:
    route, cost = line.split(" = ")
    city_a, city_b = route.split(" to ")
    G.add_edge(city_a, city_b, cost = int(cost)) 

  visited = set()
  best_cost_so_far = None
  for starting_node in G.nodes():
    visited.add(starting_node)
    cost = walk(best_cost_fn, G, starting_node, visited)
    if cost is not None:
      best_cost_so_far = cost if best_cost_so_far is None else best_cost_fn(cost, best_cost_so_far)
    visited.remove(starting_node)
  print(best_cost_so_far)


solve(min) #141
solve(max) #736
