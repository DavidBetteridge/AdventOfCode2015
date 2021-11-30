import dataclasses
from typing import List

@dataclasses.dataclass
class Ingredient :
  name: str
  capacity: int
  durability: int
  flavor: int
  texture: int
  calories: int
  quantity: int

# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
def parse_line(line: str) -> Ingredient:
  name, rest = line.split(": ")
  
  amounts = rest.split(", ")
  capacity = int(amounts[0].split(" ")[-1])
  durability = int(amounts[1].split(" ")[-1])
  flavor = int(amounts[2].split(" ")[-1])
  texture = int(amounts[3].split(" ")[-1])
  calories = int(amounts[4].split(" ")[-1])

  return Ingredient(name, capacity, durability, flavor, texture, calories, 0)

def read_file() -> List[Ingredient]:
  with open('Day15/data.txt') as f:
    return [parse_line(line.strip()) for line in f.readlines()]

ingredients = read_file()

best_total = 0
for q0 in range(1, 101):
  for q1 in range(1, 101-q0):
    for q2 in range(1, 101-q0-q1):
      ingredients[0].quantity = q0
      ingredients[1].quantity = q1
      ingredients[2].quantity = q2
      ingredients[3].quantity = 100 - (q0 + q1 + q2)

      capacity = max(0, sum([ingredient.capacity * ingredient.quantity for ingredient in ingredients]))
      durability = max(0, sum([ingredient.durability * ingredient.quantity for ingredient in ingredients]))
      flavor = max(0, sum([ingredient.flavor * ingredient.quantity for ingredient in ingredients]))
      texture = max(0, sum([ingredient.texture * ingredient.quantity for ingredient in ingredients]))
      calories = max(0, sum([ingredient.calories * ingredient.quantity for ingredient in ingredients]))
      total = capacity * durability * flavor * texture

      if calories == 500:  #Part 2
        best_total = max(best_total, total)
print(best_total)