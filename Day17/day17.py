from typing import List
from itertools import combinations

def read_file() -> List[int]:
  with open('Day17/data.txt') as f:
    return [int(line.strip()) for line in f.readlines()]

containers = read_file()    

total = sum( [  len([c for c in combinations(containers, r=size) if sum(c) == 150]) for size in range(2, len(containers)) ] )
print(total)  #1304


for size in range(2, len(containers)):
  total = len([c for c in combinations(containers, r=size) if sum(c) == 150])
  if total != 0:
    print(total)   #18
    break






