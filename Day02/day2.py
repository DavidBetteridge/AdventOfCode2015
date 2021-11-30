from typing import List, Tuple

def read_file(filename) -> List[str]:
  with open(filename) as f:
    return f.readlines()

def paper_for_box(l, w, h):
  sides = [l*w, w*h, h*l]
  return 2*sum(sides) + min(sides)

def ribbon_for_box(l, w, h):
  perimeters = [l+l+w+w, l+l+h+h, w+w+h+h]
  volume = l * w * h
  return min(perimeters) + volume

def part1(lines: List[Tuple[int,int,int]]):
  return sum([paper_for_box(*line) for line in lines])

def part2(lines: List[Tuple[int,int,int]]):
  return sum([ribbon_for_box(*line) for line in lines])


lines = read_file('Day02/data.txt')
lines = [line.rstrip().split('x') for line in lines]
lines = [ ( int(line[0]),int(line[1]),int(line[2]) ) for line in lines]  

print(part1(lines))
print(part2(lines))

