def part1():
  houses = [0] * 3310000

  for elf in range(1, 3310000):
    for house in range(elf, 3310000, elf):
      houses[house] += elf

  for no,qty in enumerate(houses):
    if qty >= 3310000:
      print(no)  #776160
      break


def part2():
  houses = [0] * 331000000

  for elf in range(1, 3310000):
    for h in range(1, 51):
      houses[elf*h] += (elf * 11)

  for no,qty in enumerate(houses):
    if qty >= 33100000:
      print(no)  #786240
      break
