houses = [0] * 3310000

for elf in range(1, 3310000):
  for house in range(elf, 3310000, elf):
    houses[house] += elf

for no,qty in enumerate(houses):
  if qty >= 3310000:
    print(no)  #776160
    break
