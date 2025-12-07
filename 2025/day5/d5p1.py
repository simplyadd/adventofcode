import sys
sys.path.append('../../')
from parser import *

class Range:
  def __init__(self, min: str, max: str):
    self.min = min
    self.max = max

  def __repr__(self):
    return f'Range({self.min}, {self.max})'

def main():
  '''"Just put the fruits in the bag" method

  A.K.A no optimizations such as combining the range of lists
  or ordering the ranges from smallest to largest'''
  ranges = []
  total = 0  # Total fresh fruits
  f = open(args.file, 'r')
  l = f.readline()

  while (l != '\n'):
    line = l.rstrip()
    try:    a, b =line.split('-')
    except: a, b = line, line
    ranges.append(Range(int(a), int(b)))
    l = f.readline()
  for l in f:
    n = int(l.rstrip())
    for r in ranges:
      logger.debug(f'Is n={n} in {r.min}-{r.max}')
      if (n >= r.min) and (n <= r.max):
        total +=1
        break

  f.close()
  logger.info(total)

if __name__ == "__main__":
  main()