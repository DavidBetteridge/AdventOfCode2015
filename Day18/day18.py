from typing import DefaultDict


def read_file() -> dict:
  with open('Day18/data.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    grid = DefaultDict(int)
    for row_number, line in enumerate(lines):
      for column_number, cell in enumerate(line):
        if cell == "#":
          grid[(column_number, row_number)] = 1
    return grid, len(lines), len(lines[0])

grid, number_of_rows, number_of_columns = read_file()

NEIGHBOURS = [(-1, -1),(0, -1),(1, -1),
              (-1,  0),        (1,  0),
              (-1,  1),(0,  1),(1,  1)]

def next(grid: dict) -> dict:
  new_grid = DefaultDict(int)

  for r in range(number_of_rows):
    for c in range(number_of_columns):
      number_of_neighbours = len([1 for (x,y) in NEIGHBOURS if grid[(c+x, r+y)] == 1 ])
      if grid[(c,r)] == 1:
        if number_of_neighbours in [2,3]:
          new_grid[(c,r)] = 1
      else:
        if number_of_neighbours == 3:
          new_grid[(c,r)] = 1
  return new_grid

def switch_on_corners(grid, number_of_rows, number_of_columns):
    grid[0,0] = 1
    grid[0,number_of_rows-1] = 1
    grid[number_of_columns-1,0] = 1
    grid[number_of_columns-1,number_of_rows-1] = 1


switch_on_corners(grid, number_of_rows, number_of_columns)
for _ in range(100):
  grid = next(grid)
  switch_on_corners(grid, number_of_rows, number_of_columns) 

print(len(grid)) #924

