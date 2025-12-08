import sys
sys.path.append('../../')
from parser import *

class Range:
  def __init__(self, low: int, high: int):
    self.low = low
    self.high = high
    self.prev = None
    self.next = None

  def __repr__(self):
    return f'Range({self.low}, {self.high}, {self.next})'

def main():
  '''"Just put the fruits in the bag" method

  A.K.A no optimizations such as combining the range of lists
  or ordering the ranges from smallest to largest'''

  total = 0  # Total fresh fruits

  f = open(args.file, 'r')
  l = f.readline()

  # # Initialize low and high with first line
  # line = l.rstrip()
  # try:    low, high =line.split('-')
  # except: low, high = line, line

  # ranges = Range(int(low), int(high))

  while (l != '\n'):
    line = l.rstrip()
    try:    a, b = line.split('-')
    except: a, b = line, line

    a, b = int(a), int(b)
    try: curr = ranges
    except:
      ranges = Range(a, b)
      l = f.readline()
      continue
    temp = Range(a, b)

    while (True):
      if (a >= curr.low):
        if (a <= curr.high):
          # curr.low <= a-b <= curr.high
          if (b <= curr.high): break
          # curr.low <= a   <  curr.high < b
          if ( (curr.next is None) or
              ((curr.next is not None) and (b < curr.next.low))):
            curr.high = b
          else: # b >= curr.next.low
            curr.high = max(curr.next.high, b)
            curr.next = curr.next.next
        elif (curr.next is not None):
          curr = curr.next
          continue
        else: curr.next = temp
        break
      # a < curr.low
      elif (b <= curr.high): # a-b <= curr.high
        if (b >= curr.low): # a < curr.low <= b <= curr.high
          if ( (curr.prev is None) or
              ((curr.prev is not None) and (a > curr.prev.high))):
              curr.low = a
        elif (curr.prev is not None): # a-b < curr.low <= curr.high
          curr = curr.prev
          continue
        else: curr.prev = temp
        break
      else:  # a < curr.low < curr.high < b
        curr.low = a
        curr.high = b
        break
    l = f.readline()

  curr = ranges
  while curr.next is not None:
    total = total + (curr.high - curr.low + 1)
    curr = curr.next
  total = total + (curr.high - curr.low + 1) # For the last range

  f.close()
  logger.debug(ranges)
  logger.info(total)

if __name__ == "__main__":
  main()