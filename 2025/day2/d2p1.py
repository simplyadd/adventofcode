import re
import sys

ranges = []

class Range:
  def __init__(self, min: str, max: str):
    self.min = min
    self.max = max

  def __repr__(self):
    return f'Range({self.min}, {self.max})'

def check_pattern(s: str) -> str | None:
    # The pattern (.+?) captures any sequence of one or more characters
    # and \1+ checks if that captured group repeats one or more times immediately after.
    pattern = r'(.+?)\1+'
    return re.search(pattern, s) is not None

def main():
  global ranges
  invIDs = [] # list of invalid IDs
  sumIDs = 0  # sum of invalid IDs

  try:
    input = open(sys.argv[1], 'r')
  except:
    input = open('input.txt', 'r')

  line1 = input.readline()

  for r in line1.split(','):
    l, h = re.findall(r'\d+', r)
    ranges.append(Range(l, h))
    
  if DEBUG_MODE:
    print(f'\nranges = {ranges}')
    print(f'\nInvalid IDs = {invIDs}\n')

  input.close()
  print(sumIDs)

if __name__ == "__main__":
  DEBUG_MODE = 1 if (sys.argv[-1]=='DEBUG') else 0
  main()