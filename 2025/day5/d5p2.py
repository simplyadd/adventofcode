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
    return f'{self.low}-{self.high}'

def main():
  '''
  Returns total number IDs of fresh fruit.

  Bugs: Does not work for test1.txt and test2.txt test cases.
  '''
  ranges = Range (0, 0)
  total = 0  # Total fresh fruits

  f = open(args.file, 'r')
  l = f.readline()
  line = l.rstrip()
  a, b = line.split('-')
  a, b = int(a), int(b)
  ranges = Range(a, b)

  while (l != '\n'):
    line = l.rstrip()
    try:    a, b = line.split('-')
    except: a, b = line, line

    a, b = int(a), int(b)
    temp = Range(a, b)
    curr = ranges

    while (True):
      if (a >= curr.low):
        if (a <= curr.high):
          # curr.low <= a-b <= curr.high
          if (b <= curr.high):
            break
          # curr.low <= a   <  curr.high < b
          if ((curr.next is None) or (b < curr.next.low)):
            curr.high = b
          else: # b >= curr.next.low
            curr.high = max(curr.next.high, b)
            curr.next = curr.next.next
        elif((curr.next is None) or
             ((a > curr.high) and (b < curr.next.low))):
          temp.prev = curr
          temp.next = curr.next
          curr.next = temp
        else:
          curr = curr.next
          continue
        break
      # a < curr.low
      elif (b <= curr.high): # a-b <= curr.high
        if (b >= curr.low): # a < curr.low <= b <= curr.high
          if ((curr.prev is None) or (a > curr.prev.high)):
            curr.low = a
          else: # b <= curr.next.low
            curr.high = min(curr.prev.low, a)
            curr.prev = curr.prev.prev
        elif ((curr.prev is None) or
              ((a > curr.prev.high) and (b < curr.low))):
          temp.prev = curr.prev
          temp.next = curr
          curr.prev = temp
          ranges = temp
        else: # a-b < curr.low <= curr.high
          curr = curr.prev
          continue
        break
      else:  # a < curr.low < curr.high < b
        curr.low = a
        curr.high = b
        break
    l = f.readline()

  curr = ranges
  while curr.next is not None:
    logger.debug(curr)
    total = total + (curr.high - curr.low + 1)
    curr = curr.next
  logger.debug(curr)
  total = total + (curr.high - curr.low + 1) # For the final range

  f.close()
  if (args.file == 'test.txt'):
    logger.info(f'Test Passed: {total == 14}')
    logger.debug(total)
  elif (args.file == 'test1.txt'):
    logger.info(f'Test Passed: {total == 202}')
    logger.debug(total)
  else:
    logger.info(total)

if __name__ == "__main__":
  main()