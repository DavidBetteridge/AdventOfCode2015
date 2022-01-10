# spells = [
#   { "name": "Magic Missile", "cost": 53, "damage": 4, "hit_points": 0, "duration": 0, "armor": 0 },
#   { "name": "Drain", "cost": 73, "damage": 2, "hit_points": 2, "duration": 0, "armor": 0 },
#   { "name": "Shield", "cost": 113, "damage": 0, "hit_points": 0, "duration": 6, "armor": 7 },
#   { "name": "Poison", "cost": 173, "damage": 3, "hit_points": 0, "duration": 6, "armor": 0 },
#   { "name": "Recharge", "cost": 229, "damage": 0, "hit_points": 0, "duration": 5, "armor": 0, "mana": 101 },
# ]


from typing import List, Tuple
import dataclasses

@dataclasses.dataclass(frozen=True)
class Player:
  hit_points: int
  mana: int
  armor: int
  damage : int

spells = [
  "Magic Missile",
  "Drain",
  "Shield",
  "Poison",
  "Recharge"
]

players_inventory = {}  #(Name: Duration remaining)

def available_spells() -> List[str]:
  #TODO Take funds into account
  return [spell for spell in spells if spell not in players_inventory ]

def attack(attacker: Player,  defender: Player) -> Player:
  #TODO: Shield 
  damage = max(1, attacker.damage - defender.armor)
  return Player(defender.hit_points - damage,  defender.mana, defender.armor, defender.damage)

def apply_spells(players_inventory: dict, player: Player, boss: Player) -> Tuple[Player, Player]:
  to_remove = []
  for spell in players_inventory:
    if spell == "Poison":
      boss = Player(boss.hit_points-3,boss.mana,boss.armor,boss.damage)
    if spell == "Recharge":
      player = Player(player.hit_points,player.mana+101,player.armor,player.damage)      
    players_inventory[spell] -= 1
    if players_inventory[spell] == 0:
      to_remove.append(spell)

    for spell in to_remove:
      players_inventory.pop(spell)
  return player, boss



player = Player(10, 250, 0, 0)
boss = Player(13,0,0,8)

# Player casts poison
players_inventory["Poison"] = 6
cost = 173
player = Player(player.hit_points,player.mana-cost,player.armor,player.damage)

# Boss's turn
player, boss = apply_spells(players_inventory, player, boss)
player = attack(boss, player)


# Player casts magic missile
player, boss = apply_spells(players_inventory, player, boss)
cost = 53
player = Player(player.hit_points,player.mana-cost,player.armor,player.damage)
boss = Player(boss.hit_points - 4,  boss.mana, boss.armor, boss.damage)

# Boss's turn
player, boss = apply_spells(players_inventory, player, boss)
if boss.hit_points <= 0:
  print("Player wins")



print(player)
print(boss)
print(players_inventory)