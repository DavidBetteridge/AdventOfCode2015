import dataclasses
import math
from typing import List

@dataclasses.dataclass
class Reindeer:
  name: str
  speed: int
  fly_time: int
  rest_time: int
  extra_points: int

def parse_line(line: str) -> Reindeer:
  parts = line.split(" ")
  name = parts[0]
  speed = int(parts[3])
  fly_time = int(parts[6])
  rest_time = int(parts[-2])
  return Reindeer(name, speed, fly_time, rest_time, 0)

def read_file() -> List[Reindeer]:
  with open('Day14/data.txt') as f:
    return [parse_line(line.strip()) for line in f.readlines()]

def distance_flown(reindeer: Reindeer, time_available: int) -> int:
  time_for_single_cycle = reindeer.rest_time + reindeer.fly_time
  number_of_complete_cycles = math.floor(time_available / time_for_single_cycle)
  fly_time_remaining = min(reindeer.fly_time, time_available % time_for_single_cycle)
  return (number_of_complete_cycles * reindeer.fly_time * reindeer.speed) + (fly_time_remaining * reindeer.speed)

reindeers = read_file()

for time_elapsed in range(2503):
  distances = [(distance_flown(r, time_elapsed+1),r) for r in reindeers]
  ordered_distances = sorted(distances, reverse=True, key=lambda d: d[0])
  i = 0
  while i < len(reindeers) and ordered_distances[0][0] == ordered_distances[i][0]:
    ordered_distances[i][1].extra_points +=1
    i += 1

print(max(r.extra_points for r in reindeers))  
