from typing import List, Tuple
import dataclasses

@dataclasses.dataclass(frozen=True)
class Player:
  hit_points: int
  mana: int

@dataclasses.dataclass(frozen=True)
class Boss:
  hit_points: int
  damage : int


spells = [
  "Magic Missile",
  "Drain",
  "Shield",
  "Poison",
  "Recharge"
]

def apply_spells(players_inventory: dict, player: Player, boss: Boss) -> Tuple[Player, Boss]:
  to_remove = []
  for spell in players_inventory:
    if spell == "Poison":
      boss = Boss(boss.hit_points-3,boss.damage)
    if spell == "Recharge":
      player = Player(player.hit_points,player.mana+101)      
    players_inventory[spell] -= 1
    if players_inventory[spell] == 0:
      to_remove.append(spell)

    for spell in to_remove:
      players_inventory.pop(spell)
  return player, boss

# def available_spells() -> List[str]:
#   #TODO Take funds into account
#   return [spell for spell in spells if spell not in players_inventory ]

players_inventory = {}  #(Name: Duration remaining)
player = Player(10, 250)
boss = Boss(13, 8)

for turn in range(2):

  # Players turn
  player, boss = apply_spells(players_inventory, player, boss)
  spell_to_use = "Poison" if turn == 0 else "Magic Missile"

  if spell_to_use == "Magic Missile":
    player = Player(player.hit_points,player.mana-53)
    boss = Boss(boss.hit_points - 4, boss.damage)
  elif spell_to_use == "Drain":
    player = Player(player.hit_points+2,player.mana-73)
    boss = Boss(boss.hit_points - 2, boss.damage)  
  elif spell_to_use == "Shield":
    player = Player(player.hit_points,player.mana-113)
    players_inventory["Shield"] = 6
  elif spell_to_use == "Poison":
    players_inventory["Poison"] = 6
    player = Player(player.hit_points,player.mana-173) 
  elif spell_to_use == "Recharge":
    players_inventory["Recharge"] = 5
    player = Player(player.hit_points,player.mana-229) 


  # Boss's turn
  armor = 7 if "Shield" in players_inventory else 0
  player, boss = apply_spells(players_inventory, player, boss)
  if boss.hit_points <= 0:
    "Player wins"
    break
  damage = max(1, boss.damage - armor)
  player = Player(player.hit_points-damage,player.mana) 


print(player)
print(boss)
print(players_inventory)