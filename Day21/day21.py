import dataclasses

@dataclasses.dataclass(frozen=True)
class Player:
  hit_points: int
  damage : int
  armor: int


def attack(attacker: Player,  defender: Player) -> Player:
  damage = max(1, attacker.damage - defender.armor)
  return Player(defender.hit_points - damage, defender.damage, defender.armor)

def does_player_wins(player, boss) -> bool:
  while boss.hit_points > 0 and player.hit_points > 0:
    boss = attack(player, boss)
    if boss.hit_points <= 0:
      return True
    player = attack(boss, player)
    if player.hit_points <= 0:
      return False


weapons = [
  { "name": "Dagger", "Cost": 8, "Damage" : 4, "Armor": 0 },
  { "name": "Shortsword", "Cost": 10, "Damage" : 5, "Armor": 0 },
  { "name": "Warhammer", "Cost": 25, "Damage" : 6, "Armor": 0 },
  { "name": "Longsword", "Cost": 40, "Damage" : 7, "Armor": 0 },
  { "name": "Greataxe", "Cost": 74, "Damage" : 8, "Armor": 0 },
]

armors = [
  { "name": "None", "Cost": 0, "Damage" : 0, "Armor": 0 },
  { "name": "Leather", "Cost": 13, "Damage" : 0, "Armor": 1 },
  { "name": "Chainmail", "Cost": 31, "Damage" : 0, "Armor": 2 },
  { "name": "Splintmail", "Cost": 53, "Damage" : 0, "Armor": 3 },
  { "name": "Bandedmail", "Cost": 75, "Damage" : 0, "Armor": 4 },
  { "name": "Platemail", "Cost": 102, "Damage" : 0, "Armor": 5 },
]

rings = [
  { "name": "None", "Cost": 0, "Damage" : 0, "Armor": 0 },
  { "name": "Damage +1", "Cost": 25, "Damage" : 1, "Armor": 0 },
  { "name": "Damage +2", "Cost": 50, "Damage" : 2, "Armor": 0 },
  { "name": "Damage +3", "Cost": 100, "Damage" : 3, "Armor": 0 },
  { "name": "Defense +1", "Cost": 20, "Damage" : 0, "Armor": 1 },
  { "name": "Defense +2", "Cost": 40, "Damage" : 0, "Armor": 2 },
  { "name": "Defense +3", "Cost": 80, "Damage" : 0, "Armor": 3 },
]

lowest_gold = 9999999999
highest_gold = 0

for weapon in weapons:
  for armor in armors:
    for ring0 in rings:
      for ring1 in rings:
        if ring0["name"] not in ["", ring1["name"]]:
          gold = weapon["Cost"] + armor["Cost"] + ring0["Cost"] + ring1["Cost"]
          damage = weapon["Damage"] + armor["Damage"] + ring0["Damage"] + ring1["Damage"]
          armor_points = weapon["Armor"] + armor["Armor"] + ring0["Armor"] + ring1["Armor"]
          player = Player(100, damage, armor_points)
          boss = Player(100, 8, 2)
          if does_player_wins(player, boss):
            lowest_gold = min(lowest_gold, gold)
          else:
            highest_gold = max(highest_gold, gold)

print(lowest_gold)  #91
print(highest_gold)  #158