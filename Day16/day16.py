import operator
from typing import Dict, List, Tuple

def parse_line(line: str) -> Tuple[int, Dict[str, int]]:
  split_at = line.index(":")
  no = int(line[:split_at].split(" ")[-1])
  rest = line[split_at+2:]
  
  values = rest.split(", ")
  d = {}
  for value in values:
    name, qty = value.split(": ")
    d[name] = int(qty)

  return no,  d

def read_file() -> List[Tuple[int, Dict[str, int]]]:
  with open('Day16/data.txt') as f:
    return [parse_line(line.strip()) for line in f.readlines()]

def filter_sues(current: List[Tuple[int, Dict[str, int]]],
                field_name: str, value: int, operator_fn: callable) \
                                              -> List[Tuple[int, Dict[str, int]]]:
  return [sue for sue in current
          if field_name not in sue[1] or operator_fn(sue[1][field_name], value) ]

sues = read_file()
sues = filter_sues(sues, "children", 3, operator.eq)
sues = filter_sues(sues, "cats", 7, operator.gt)
sues = filter_sues(sues, "samoyeds", 2, operator.eq)
sues = filter_sues(sues, "pomeranians", 3, operator.lt)
sues = filter_sues(sues, "akitas", 0, operator.eq)
sues = filter_sues(sues, "vizslas", 0, operator.eq)
sues = filter_sues(sues, "goldfish", 5, operator.lt)
sues = filter_sues(sues, "trees", 3, operator.gt)
sues = filter_sues(sues, "cars", 2, operator.eq)
sues = filter_sues(sues, "perfumes", 1, operator.eq)
print(sues)