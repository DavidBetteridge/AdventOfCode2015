
from typing import DefaultDict, Tuple


def read_file() -> Tuple[dict, str]:
  with open('C:\Personal\AdventOfCode2015\Day19\data.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    
    replacements = DefaultDict(list)
    for line in lines[:-2]:
        lhs, rhs = line.split(" => ")
        replacements[lhs].append(rhs)

    medicine_molecule = lines[-1]
    return replacements, medicine_molecule

replacements, medicine_molecule = read_file()

 
def part_one():
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


def part_two():
  reverse_replacements = {rhs:lhs 
        for lhs in replacements
        for rhs in replacements[lhs]}
  lookup = sorted(reverse_replacements, key=lambda s: len(s), reverse=True)

  number_of_replacements = 0
  molecule = medicine_molecule
  while molecule != "e":
    for rhs in lookup:
      start_index = molecule.find(rhs)
      if start_index != -1:
        molecule = molecule[:start_index] + reverse_replacements[rhs] + molecule[start_index+len(rhs):]
        number_of_replacements+=1
        break

  print(number_of_replacements)    #212


part_one()
part_two()