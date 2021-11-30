from typing import DefaultDict, List

def read_file() -> List[str]:
  with open('Day03/data.txt') as f:
    return f.read()


directions = read_file()
visited = DefaultDict(int)
current_x = 0
current_y = 0

visited[(current_x, current_y)] = 1

for direction in directions:
  if direction == "v":
    current_y -= 1
  elif direction == "^":
    current_y += 1
  elif direction == "<":
    current_x -= 1
  elif direction == ">":
    current_x += 1    
  visited[(current_x, current_y)] += 1

print(len(visited))
