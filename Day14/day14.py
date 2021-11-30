import dataclasses
import math
from typing import List

@dataclasses.dataclass(frozen=True)
class Reindeer:
  name: str
  speed: int
  fly_time: int
  rest_time: int

def parse_line(line: str) -> Reindeer:
  parts = line.split(" ")
  name = parts[0]
  speed = int(parts[3])
  fly_time = int(parts[6])
  rest_time = int(parts[-2])
  return Reindeer(name, speed, fly_time, rest_time)

def read_file() -> List[Reindeer]:
  with open('Day14/data.txt') as f:
    return [parse_line(line.strip()) for line in f.readlines()]

def distance_flown(reindeer: Reindeer, time_available: int) -> int:
  time_for_single_cycle = reindeer.rest_time + reindeer.fly_time
  number_of_complete_cycles = math.floor(time_available / time_for_single_cycle)
  fly_time_remaining = min(reindeer.fly_time, time_available % time_for_single_cycle)
  return (number_of_complete_cycles * reindeer.fly_time * reindeer.speed) + (fly_time_remaining * reindeer.speed)

reindeers = read_file()
print(max(distance_flown(r, 2503) for r in reindeers))  #2696
