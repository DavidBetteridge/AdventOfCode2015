
from typing import DefaultDict, Tuple


def read_file() -> Tuple[dict, str]:
  with open('Day19/data.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    
    replacements = DefaultDict(list)
    for line in lines[:-2]:
        lhs, rhs = line.split(" => ")
        replacements[lhs].append(rhs)

    medicine_molecule = lines[-1]
    return replacements, medicine_molecule


replacements, medicine_molecule = read_file()

possible_strings = set()
i = 0
while i < len(medicine_molecule):
  if medicine_molecule[i] in replacements:
    for replacement in replacements[medicine_molecule[i]]:
      temp = medicine_molecule[:i] + replacement + medicine_molecule[i+1:]
      possible_strings.add(temp)
  elif i+1 < len(medicine_molecule) and medicine_molecule[i:i+2] in replacements:
    for replacement in replacements[medicine_molecule[i:i+2]]:
      temp = medicine_molecule[:i] + replacement + medicine_molecule[i+2:]
      possible_strings.add(temp)      
  i+=1

print(len(possible_strings))      #535

