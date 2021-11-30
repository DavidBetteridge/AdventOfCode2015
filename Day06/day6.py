from collections import Counter
from typing import DefaultDict, List


def read_file() -> List[str]:
  with open('Day06/data.txt') as f:
    return f.readlines()

lines = read_file()
grid = DefaultDict(bool)
for line in lines:
  if line.startswith("turn on"):
    command = "ON"
    rest = line[len("turn on")+1:]
  elif line.startswith("turn off"):
    command = "OFF"
    rest = line[len("turn off")+1:]    
  elif line.startswith("toggle"):
    command = "TOGGLE"
    rest = line[len("toggle")+1:]        
  else:
    raise Exception("Unknown command")
  bl, tr = rest.split(" through ")
  x0, y0 = bl.split(",")
  x1, y1 = tr.split(",")

  for x in range(int(x0), int(x1)+1):
    for y in range(int(y0), int(y1)+1):
      if command == "ON":
        grid[(x,y)]=True
      elif command == "OFF":
        grid[(x,y)]=False
      else:
        grid[(x,y)]=not grid[(x,y)]

print(Counter(grid.values()))

  