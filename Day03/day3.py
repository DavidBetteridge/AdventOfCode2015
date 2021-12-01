from typing import List

def read_file() -> List[str]:
  with open('Day03/data.txt') as f:
    return f.read()

def move(direction, current):
  if direction == "v":
    current = (current[0], current[1] - 1)
  elif direction == "^":
    current = (current[0], current[1] + 1)
  elif direction == "<":
    current = (current[0] - 1, current[1])
  elif direction == ">":
    current = (current[0] + 1, current[1])
  return current

def common(number_of_workers: int):
  directions = read_file()
  visited = set()
  workers = [(0,0)] * number_of_workers
  visited.add((0,0))
  worker_number = 0

  for direction in directions:
    workers[worker_number] = move(direction, workers[worker_number])
    visited.add(workers[worker_number])
    worker_number = (worker_number + 1) % number_of_workers
  
  print(len(visited))

common(1) #2572
common(2) #2631 