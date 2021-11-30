import re
from collections import Counter
from typing import List

def read_file() -> List[str]:
  with open('Day08/data.txt') as f:
    return [line.strip() for line in f.readlines()]

def in_memory_size(line: str) -> int:
  base = line[1:-1]
  number_of_backslashes = len(re.findall(r'\\\\', base))
  number_of_quotes = len(re.findall('\\\"', base))
  number_of_hex = len(re.findall(r"\\x[0-9a-f]{2}", base))
  return len(base) - number_of_quotes - number_of_backslashes - (number_of_hex * 3)

def encode(line: str) -> int:
  counters = Counter(line)
  number_of_quotes = counters["\""]
  number_of_backslashes = counters["\\"]
  return len(line) + 2 + number_of_backslashes + number_of_quotes

lines = read_file()
print(sum([len(line) - in_memory_size(line) for line in lines])) #1333
print(sum([encode(line) - len(line) for line in lines])) #2046
