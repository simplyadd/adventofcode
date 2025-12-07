import re
import sys
sys.path.append('../../')
from parser import *

threeLines = ['', '']
total = 0

def check_if_accessible(start: int) -> bool:
  global threeLines
  adjacent = -1

  for i in threeLines:
    try:    adjacent += count_adjacent(i, start)
    except: break

    if (adjacent >= 4): return False
  return True

def count_adjacent(line: str, start: int) -> int:
  adj = 0
  min = start-1 if (start !=0) else start
  max = start+2 if (start < line_len-1) else line_len
  for i in line[min:max]:
    if i != '.':
      adj += 1
  return adj


def find_rolls(line: str):
  global total
  for roll in re.finditer(r'@', line):
    index = roll.start() # Returns index of matched str
    found = check_if_accessible(index)
    if (found): total += 1
  return

def find_rolls_dbg(line: str):
  global total
  test  = ''
  for i, c in enumerate(line):
    if (c == '@'): found = check_if_accessible(i)
    else:          found = False

    if (found):
      total += 1
      test += 'x'
    else: test += line[i]
  logger.debug(test)
  return

def main():
  global threeLines
  global total

  logger.debug('----------DEBUG MODE START----------')
  input = open(args.file, 'r')

  line1 = input.readline()
  threeLines.append(line1.rstrip())

  for line in input:
    threeLines.append(line.rstrip()) # Add new index
    threeLines.pop(0)                # Keep length at 3

    # Iterates through the whole string when debugging
    find_rolls_dbg(threeLines[1]) if (log_level==logging.DEBUG) else find_rolls(threeLines[1])

  # For last line
  threeLines.pop(0)
  find_rolls_dbg(threeLines[1]) if (log_level==logging.DEBUG) else find_rolls(threeLines[1])

  input.close()
  logger.debug('----------DEBUG MODE END------------')
  logger.info(total)

if __name__ == "__main__":
  # Get length of first line before starting
  input = open(args.file, 'r')
  line_len = len(input.readline().rstrip())
  input.close()
  main()