import networkx as nx
from typing import List, Optional, Set


def read_file() -> List[str]:
  with open('Day13/data.txt') as f:
    return [line.strip() for line in f.readlines()]

def seat(G : nx.Graph, currentNode: str, seated: List[str]) -> Optional[int]:
  if len(seated) == len(G.nodes()):
    # We have completed the table.  Score up the edges
    total = 0
    for i in range(len(seated)):
      p0 = seated[i]
      p1 = seated[(i + 1) % len(seated)]
      total += G.edges[p0,p1]["cost"]
      total += G.edges[p1,p0]["cost"]
    return total
  
  available_people = G.edges(currentNode, data=True)
  best_cost_so_far = 0  
  for _, person, _ in available_people:
    if person not in seated:
      seated.append(person)
      cost = seat(G, person, seated)
      best_cost_so_far = max(cost, best_cost_so_far)      
      seated.remove(person)
  return best_cost_so_far

# Bob would gain 83 happiness units by sitting next to Alice.
# Bob would lose 7 happiness units by sitting next to Carol.
def solve():
  G = nx.DiGraph()
  lines = read_file()
  for line in lines:
    person1 = line[:line.index(" ")]
    person2 = line[line.rindex(" ")+1:-1]
    if " gain " in line:
      cost = int(line.split(" ")[3])
    else:
      cost = -int(line.split(" ")[3])

    G.add_edge(person1, person2, cost = cost) 
    G.add_edge(person1, "ME", cost = 0) #Part 2
    G.add_edge("ME", person1, cost = 0) #Part 2

  first_seat = lines[0][:lines[0].index(" ")]
  seated = [first_seat]
  cost = seat(G, first_seat, seated)
  print(cost)


solve()
