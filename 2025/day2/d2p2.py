import re
import sys


# FIXME: Remove this function
def check_pattern(s: str) -> bool:
  '''
  The pattern (.+?) captures any sequence of one or more characters and \1+
  checks if that captured group repeats one or more times immediately after.

  :param s: string to check for pattern
  :type s: str
  :return: True if valid pattern and false if invalid (empty string)
  :rtype: bool
  '''

  found = re.search(r'(.+?)\1+', s)
  if (found):
    # search() returns a match object so it needs to be joined to get str
    pattern = found.group()
    new_text = re.sub(pattern, '', s)
  else:
    new_text = ''
  return (new_text != '')


def get_new_num(num: str) -> int:
  '''
  Updated to not skip odd length numbers (except for a length of 1)
  and return the next likely invalid string.

  :param num: Number in string format to parse
  :type num: str
  :return: Next likely invalid string
  :rtype: int
  '''

  lnum = len(num)
  if lnum == 1:
    return 11
  elif (lnum & 1):
    tri = lnum // 3
    part1 = num[:tri]
    part2 = num[tri:tri*2]
    part3 = num[tri*2:]

    if (part1 == part2 == part3):
      return int(num)       # Return invalid pattern as is
    if ((int(part1) > int(part2)) or
        (int(part1) > int(part3))):
      return int(part1 * 3) # Return next invalid pattern
  else:
    mid   = lnum // 2
    part1 = num[:mid]
    part2 = num[mid:]

    if (part1 == part2):
      return int(num)       # Return invalid pattern as is
    if int(part1) > int(part2):
      return int(part1 * 2) # Return next invalid pattern

  return int(num) + 1   # Give up optimizing


def main():
  '''
  Print the sum of all invalid IDs from a list of ranges.
  Invalid IDs are numbers with a repeating pattern.
  '''

  invIDs = [] # list of invalid IDs
  sumIDs = 0  # sum of invalid IDs

  try:
    input = open(sys.argv[1], 'r')
  except:
    input = open('input.txt', 'r')

  line1 = input.readline()

  for r in line1.split(','):
    l, h = re.findall(r'\d+', r)

    curr = int(l)
    while (curr <= int(h)):
      if not (check_pattern(str(curr))):
        invIDs.append(curr)
        sumIDs += curr
        curr += 1
      curr = get_new_num(str(curr))

  input.close()
  if DEBUG_MODE:
    print(f'\nInvalid IDs = {invIDs}\n')

  if DEBUG_TEST: # when input file is test.txt
    print(f'Test Passed: {sumIDs == 4174379265}')
  else:
    print(sumIDs)

if __name__ == "__main__":
  DEBUG_MODE = 1 if (sys.argv[-1]=='DEBUG') else 0
  DEBUG_TEST = 1 if (sys.argv[-1]=='DTEST') else 0
  main()