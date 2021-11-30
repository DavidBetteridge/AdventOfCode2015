
from typing import List


def read_file() -> List[str]:
  with open('Day23\data.txt') as f:
    return [line.strip() for line in f.readlines()]

instructions = read_file()
reg_a = 1
reg_b = 0

def read_register(register: str) -> int:
  if register == "a":
    return reg_a
  elif register == "b":
    return reg_b
  else:
    raise ValueError(register)

def set_register(register: str, new_value: int):
  global reg_a
  global reg_b
  if register == "a":
    reg_a = new_value
  elif register == "b":
    reg_b = new_value
  else:
    raise ValueError(register)

ip = 0
while ip < len(instructions):
  instruction = instructions[ip]
  parts = instruction.split(" ")
  operand1 = parts[1]
  if operand1.endswith(","): operand1 = operand1[:-1]

  operator = parts[0]
  
  if operator == "inc":
    current_value = read_register(operand1)
    set_register(operand1, current_value+1)
    ip += 1

  elif operator == "hlf":
    current_value = read_register(operand1)
    set_register(operand1, current_value / 2)
    ip += 1

  elif operator == "tpl":
    current_value = read_register(operand1)
    set_register(operand1, current_value * 3)
    ip += 1

  elif operator == "jmp":
    ip += int(operand1)    

  elif operator == "jie":
    is_even = read_register(operand1) % 2 == 0
    if is_even:
      ip += int(parts[2])   
    else:
      ip += 1

  elif operator == "jio":
    is_one = read_register(operand1) == 1
    if is_one:
      ip += int(parts[2])
    else:
      ip += 1      

print(reg_a)
print(reg_b)