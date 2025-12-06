import re
import sys

class Invalid_IDs:
  def __init__(self):
    self.invIDs = []
    self.sumIDs = 0

  def __repr__(self):
    return f'\nInvalid IDs = {self.invIDs}\n\nSum of Invalid IDs = {self.sumIDs}'

  def __str__(self):
    return f'Sum of Invalid IDs = {self.sumIDs}'

  def add_id(self, num: int):
    self.invIDs.append(num)
    self.sumIDs += num

  def get_sum(self) -> int:
    return self.sumIDs

inv = Invalid_IDs()

def get_new_num(num: str) -> int:
  '''
  Updated to not skip odd length numbers (except for a length of 1)
  and return the next invalid number or next number.

  :param num: Number in string format to parse
  :type num: str
  :return: Next invalid number or next number
  :rtype: int
  '''

  inum, lnum= int(num), len(num)

  if (lnum & 1):
    # Odd length
    # length = 1 are all valid so return 11 as the next invalid number
    if lnum == 1: return 11
    # length = 5 or 7 will return a pattern of the next repeating number
    elif ((lnum == 5) or (lnum == 7)):
      new_text = re.sub(num[0], '', num)
      if (new_text == ''): inv.add_id(inum)
      c = num[0]
      if c != '9':
        pattern = str(int(c) + 1)
        return int(pattern * lnum)
    # length = 9+ (odd only)
    else:
      tri = lnum // 3
      part1 = num[:tri]
      part2 = num[tri:tri*2]
      part3 = num[tri*2:]

      if (part1 == part2 == part3): inv.add_id(inum)
      elif (int(part1) > int(part2)): return int(part1 * 3) # Return next invalid pattern
  else:
    # Even length
    mid   = lnum // 2
    part1 = num[:mid]
    part2 = num[mid:]

    if (part1 == part2): inv.add_id(inum)
    elif ((mid & 1) and (mid != 1)):
      # If half length is odd, check if first two characters are repeating
      cc = num[:2]
      new_text = re.sub(cc, '', num)
      if (new_text == ''):
        inv.add_id(inum)
    elif (int(part1) > int(part2)): return int(part1 * 2) # Return next invalid pattern
  return (inum + 1) # Give up optimizing

def main():
  '''
  Print the sum of all invalid IDs from a list of ranges.
  Invalid IDs are numbers with a repeating pattern.
  '''

  try:
    input = open(sys.argv[1], 'r')
  except:
    input = open('input.txt', 'r')

  line1 = input.readline()

  for r in line1.split(','):
    l, h = re.findall(r'\d+', r)

    curr = int(l)
    while (curr <= int(h)):
      curr = get_new_num(str(curr))

  input.close()
  if DEBUG_MODE:
    print(repr(inv))
  elif DEBUG_TEST: # when input file is test.txt
    print(f'Test Passed: {inv.get_sum() == 4174379265}')
  else:
    print(inv)

if __name__ == "__main__":
  DEBUG_MODE = 1 if (sys.argv[-1]=='DEBUG') else 0
  DEBUG_TEST = 1 if (sys.argv[-1]=='DTEST') else 0
  main()