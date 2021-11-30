from typing import Counter, List


def read_file() -> List[str]:
  with open('Day05/data.txt') as f:
    return f.readlines()

def line_is_nice(line: str) -> bool:
  counts = Counter(line)
  vowels = counts['a'] + counts['e'] + counts['i'] + counts['o'] + counts['u']
  if vowels < 3:
    return False
  elif 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
    return False
  else:
    for i in range(len(line) - 1):
      if line[i] == line[i+1]:
        return True
    return False

lines = read_file()
print(len([line for line in lines if line_is_nice(line)]))