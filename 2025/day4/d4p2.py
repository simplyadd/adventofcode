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

def find_rolls(line: str) -> str:
  global total

  test  = ''
  for i, c in enumerate(line):
    if (c == '@'): found = check_if_accessible(i)
    else:          found = False

    if (found):
      total += 1
      test += '.'
    else: test += str(line[i])
  logger.debug(test)
  return test

def main():
  global threeLines, total
  r = 0 # file position for reading the file

  logger.debug('----------DEBUG MODE START----------')

  f = open(args.file, 'a+')
  f.seek(0) # a+ mode starts at the bottom of file.
  line1 = f.readline()
  threeLines.append(line1.rstrip())

  r = r + line_len + 2
  f.write(('.' * line_len) + '\n')
  f.seek(r) # go back to correct placement

  for line in f:
    threeLines.append(line.rstrip()) # Add new index
    threeLines.pop(0)                # Keep length at 3

    new_line = find_rolls(threeLines[1])
    r = r + line_len + 2
    f.write(new_line + '\n')
    f.seek(r) # go back to correct placement

  f.close()
  logger.debug('----------DEBUG MODE END------------')
  logger.info(total)

if __name__ == "__main__":
  # Get length of first line before starting
  f = open(args.file, 'r')
  line_len = len(f.readline().rstrip())
  read_len = len(f.readline())
  f.close()
  main()