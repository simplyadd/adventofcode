import re
import sys

def validate_num(num: str) -> bool:
  lnum = len(num)
  mid = lnum // 2

  part1 = num[:mid]
  part2 = num[mid:]
  return False if (part1 == part2) else True

def get_new_num(num: str) -> int:
  lnum = len(num)
  mid = lnum // 2
  if (lnum & 1):
    # All odd length does not fit the pattern for invalid numbers
    # Get the next invalid pattern
    return int(('1' + ('0' * mid)) * 2)
  else:
    part1 = num[:mid]
    part2 = num[mid:]

    if (part1 == part2):
      return int(num)       # Return invalid pattern as is
    elif int(part1) > int(part2):
      return int(part1 * 2) # Return next invalid pattern
    else:
      part1_new = str(int(part1) + 1)
      if lnum == len(part1_new):
        return int(part1_new + part2)
      else:
        return int(num) + 1 # Give up optimizing

def main():
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
      if not (validate_num(str(curr))):
        invIDs.append(curr)
        sumIDs += curr
        curr += 1
      curr = get_new_num(str(curr))

  input.close()
  if DEBUG_MODE:
    print(f'\nInvalid IDs = {invIDs}\n')

  if DEBUG_TEST: # when input file is test.txt
    print(f'Test Passed: {sumIDs == 1227775554}')
  else:
    print(sumIDs)

if __name__ == "__main__":
  DEBUG_MODE = 1 if (sys.argv[-1]=='DEBUG') else 0
  DEBUG_TEST = 1 if (sys.argv[-1]=='DTEST') else 0
  main()