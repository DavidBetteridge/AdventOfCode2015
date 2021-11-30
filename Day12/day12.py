import json
import re
from typing import List

def read_file() -> str:
  with open('Day12/data.json') as f:
    return f.read().strip()

input = read_file()
numbers = re.findall(r'[-0-9]+', input)
print(sum([int(n) for n in numbers]))  #191164

def walk_list(values: List) -> int:
  return sum(process(array_entry) for array_entry in values)

def process(array_entry) -> int:
  if isinstance(array_entry, list):
    return walk_list(array_entry)
  elif isinstance(array_entry, dict):
    if "red" in array_entry.values():
      return 0
    else:
      return walk_list(array_entry.values())
  elif isinstance(array_entry, int):
    return int(array_entry)
  else:
    # Ignore strings
    return 0

as_json = json.loads(input)
print(walk_list(as_json))  #87842

