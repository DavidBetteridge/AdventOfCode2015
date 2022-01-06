import re

def read_file() -> str:
  with open('Day12/data.txt') as f:
    return f.read().strip()

input = read_file()
print(input)

numbers = re.findall(r'[-0-9]+', input)
print(numbers)
print(sum([int(n) for n in numbers]))