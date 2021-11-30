from typing import List

def read_file() -> List[str]:
  with open('Day05/data.txt') as f:
    return f.readlines()

def line_is_nice(line: str) -> bool:
  
  rule1 = False
  for i in range(len(line)-4):
    first = line[i:i+2]
    if line.find(first, i+2) != -1:
      rule1 = True
      break

  if not rule1: return False

  for i in range(len(line)-2):
    if line[i] == line[i+2]:
      return True
  return False

lines = read_file()
print(len([line for line in lines if line_is_nice(line)]))