from typing import DefaultDict, List

def read_file() -> List[str]:
  with open('Day03/data.txt') as f:
    return f.read()


def part1():
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


def part2():
  directions = read_file()
  visited = set()
  
  santa = (0,0)
  robot = (0,0)
  visited.add((0,0))

  santas_turn = True

  for direction in directions:
    current = santa if santas_turn else robot

    if direction == "v":
      current = (current[0], current[1] - 1)
    elif direction == "^":
      current = (current[0], current[1] + 1)
    elif direction == "<":
      current = (current[0] - 1, current[1])
    elif direction == ">":
      current = (current[0] + 1, current[1])   
    visited.add(current)

    if santas_turn:
      santa = current
    else:
      robot = current

    santas_turn = not santas_turn
  
  print(len(visited))

part2()