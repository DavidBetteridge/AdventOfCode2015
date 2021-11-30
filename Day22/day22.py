import dataclasses
from typing import List, Tuple
from copy import copy
from functools import lru_cache

@dataclasses.dataclass(frozen=True)
class Player:
  hit_points: int
  mana: int

@dataclasses.dataclass(frozen=True)
class Boss:
  hit_points: int
  damage : int


spells = [
  "Poison",
  "Recharge",
  "Shield",
  "Drain",
  "Magic Missile",
]

cost = {
  "Recharge" : 229,
  "Poison" : 173,
  "Magic Missile" : 53,
  "Drain" : 73,
  "Shield" : 113,
}

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

def available_spells(player: Player, inventory: dict) -> List[str]:
  return [spell for spell in spells if spell not in inventory and cost[spell] <= player.mana ]

lowest_cost = 1000000

def next_round(current_player: Player, current_boss: Boss, current_inventory: dict, spent):
  global lowest_cost
  current_player = Player(current_player.hit_points-1,current_player.mana) #Part2
  if current_player.hit_points <= 0: return #Boss has won

  current_player, current_boss = apply_spells(current_inventory, current_player, current_boss)

  available = available_spells(current_player, current_inventory)
  if len(available) == 0: return   #Boss has won

  for spell_to_use in available:
     # Players turn
    inventory = copy(current_inventory)  
    player = copy(current_player)  
    boss = copy(current_boss)  

    spell_cost = cost[spell_to_use]
    player = Player(player.hit_points,player.mana-spell_cost)

    if spell_to_use == "Magic Missile":
      boss = Boss(boss.hit_points - 4, boss.damage)
    elif spell_to_use == "Drain":
      player = Player(player.hit_points+2,player.mana)
      boss = Boss(boss.hit_points - 2, boss.damage)  
    elif spell_to_use == "Shield":
      inventory["Shield"] = 6
    elif spell_to_use == "Poison":
      inventory["Poison"] = 6
    elif spell_to_use == "Recharge":
      inventory["Recharge"] = 5

    if boss.hit_points <= 0: 
      if spent + spell_cost < lowest_cost:
        lowest_cost = spent + spell_cost
        print(lowest_cost)
      continue  #Player won

    # Boss's turn
    armor = 7 if "Shield" in inventory else 0
    player, boss = apply_spells(inventory, player, boss)
    if boss.hit_points <= 0:
      if spent + spell_cost < lowest_cost:
        lowest_cost = spent + spell_cost
        print(lowest_cost)
      continue  #Player won      
    damage = max(1, boss.damage - armor)
    player = Player(player.hit_points-damage,player.mana) 
    if player.hit_points <= 0: continue  #Boss won

    # Keep playing
    next_round(player, boss, inventory, spent + spell_cost)


players_inventory = {}  #(Name: Duration remaining)
player = Player(50, 500)
boss = Boss(55, 8)
next_round(player, boss, players_inventory, 0)
print(lowest_cost)

# Part 1 - 953
# Part 2 - 1289