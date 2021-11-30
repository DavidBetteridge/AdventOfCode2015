import dataclasses
from typing import DefaultDict, List, Optional

@dataclasses.dataclass(frozen=True)
class Connection:
  operator: str
  output: str
  lhs: str
  rhs: Optional[str]


def parse_connection(line: str) -> Connection:
  rhs = None
  i, o = line.strip().split(" -> ")
  
  if "AND" in i:
    lhs, rhs = i.split(" AND ")
    operator="AND"
  elif "OR" in i:
    lhs, rhs = i.split(" OR ")
    operator="OR"
  elif "LSHIFT" in i:
    lhs, rhs = i.split(" LSHIFT ")
    operator="LSHIFT"
  elif "RSHIFT" in i:
    lhs, rhs = i.split(" RSHIFT ")
    operator="RSHIFT"
  elif "NOT" in i:
    lhs = i[len("NOT "):]
    operator="NOT"
  else:
    lhs = i
    operator="ASSIGN"
  return Connection(operator, o, lhs, rhs)


def read_file() -> List[Connection]:
  with open('Day07/data.txt') as f:
    return [parse_connection(line) for line in f.readlines()]


def read_value(name: str) -> int:
  if name.isdigit():
    return int(name)
  else:
    return signals[name]

def bitwise_not(value: int) -> int:
  as_binary = (bin(value)[2:]).zfill(16)
  inverted = "".join(["1" if int(b) == 0 else "0" for b in as_binary])
  return int(inverted,2)

connections = read_file()

connectionsByInput: dict[str, List[Connection]] = DefaultDict(list)
for connection in connections:
  connectionsByInput[connection.lhs].append(connection)
  if connection.rhs:
    connectionsByInput[connection.rhs].append(connection)

signals: dict[str,int] = {}
done = set()
to_process = []

for connection in connections:
  if connection.lhs.isdigit() and connection.operator == "ASSIGN":
    signals[connection.output] = int(connection.lhs)
    to_process.append(connection.output)

# For part 2
signals["b"] = 46065

while len(to_process) > 0:
  latest_output = to_process.pop()
  if latest_output not in done:
    done.add(latest_output)
    connections_to_test = connectionsByInput[latest_output]
    for connection_to_test in connections_to_test:
      if (connection_to_test.lhs.isdigit() or connection_to_test.lhs in signals) and \
        (connection_to_test.rhs is None or connection_to_test.rhs.isdigit() or connection_to_test.rhs in signals):

        if connection_to_test.operator == "AND":
          signals[connection_to_test.output] = read_value(connection_to_test.lhs) & read_value(connection_to_test.rhs)
          to_process.append(connection_to_test.output)
        elif connection_to_test.operator == "OR":
          signals[connection_to_test.output] = read_value(connection_to_test.lhs) | read_value(connection_to_test.rhs)
          to_process.append(connection_to_test.output)
        elif connection_to_test.operator == "LSHIFT":
          signals[connection_to_test.output] = read_value(connection_to_test.lhs) << read_value(connection_to_test.rhs)
          to_process.append(connection_to_test.output)
        elif connection_to_test.operator == "RSHIFT":
          signals[connection_to_test.output] = read_value(connection_to_test.lhs) >> read_value(connection_to_test.rhs)
          to_process.append(connection_to_test.output)
        elif connection_to_test.operator == "NOT":
          signals[connection_to_test.output] = bitwise_not(read_value(connection_to_test.lhs))
          to_process.append(connection_to_test.output)
        elif connection_to_test.operator == "ASSIGN":
          signals[connection_to_test.output] = read_value(connection_to_test.lhs)
          to_process.append(connection_to_test.output)

print(signals["a"])  #46065  14134

