from collections import Counter
from typing import List


def read_file() -> List[str]:
  with open('Day08/data.txt') as f:
    return [line.strip() for line in f.readlines()]



def in_memory_size(line: str) -> int:
  base = line[1:-1]
  number_of_quotes = (len(base) - len(base.replace('\\"', ""))) / 2
  number_of_backslashes = (len(base) - len(base.replace('\\\\', ""))) / 2

  number_of_hex = 0
  for i in range(len(base)-3):
    if base[i] == "\\" and base[i+1] == "x" and base[i+2] in "0123456789abcdef" and base[i+3] in "0123456789abcdef":
      number_of_hex +=1

  return len(base) - number_of_quotes - number_of_backslashes - (number_of_hex * 3)

def encode(line: str) -> int:
  counters = Counter(line)
  number_of_quotes = counters["\""]
  number_of_backslashes = counters["\\"]
  return len(line) + 2 + number_of_backslashes + number_of_quotes


lines = read_file()
print(sum([len(line) - in_memory_size(line) for line in lines])) #1333

print(sum([encode(line) - len(line) for line in lines])) #2046
