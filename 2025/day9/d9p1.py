import sys
sys.path.append('../../')
from parser import *

def get_area(p1 : list, p2 : list) -> int:
  x = abs(p2[0]-p1[0]) + 1
  y = abs(p2[1]-p1[1]) + 1
  a = x * y
  return max(a, x, y)

def main():
  f     = open(args.file, 'r')
  tiles = []
  max_a = 0   # Largest area between red tiles

  for line in f:
    x, y = line.split(',')
    p2   = [int(x), int(y)]
    for p1 in tiles:
      a     = get_area(p1, p2)
      max_a = max(a, max_a)
    tiles.append(p2)
  logger.info(max_a)
  f.close()

if __name__ == "__main__":
  main()