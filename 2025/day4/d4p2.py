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

def parse_file(r_file, w_file):
  global threeLines

  r_file.seek(0)
  w_file.seek(0)
  w_file.truncate(0)

  line1 = r_file.readline()
  threeLines.append(line1.rstrip())

  for line in r_file:
    threeLines.append(line.rstrip()) # Add new index
    threeLines.pop(0)                # Keep length at 3
    new_line = find_rolls(threeLines[1])
    w_file.write(new_line + '\n')
  # For last line
  threeLines.pop(0)
  new_line = find_rolls(threeLines[1])
  w_file.write(new_line + '\n')
  threeLines.append('')

def parse_file_eq(f1, f2):
  r = 0

  for l1 in f1:
    r = r + line_len + 2
    f2.seek(r)
    l2 = f2.readline()
    if (l1 != l2):
      return True
  return False

def main():
  global threeLines
  global total
  r = 0 # file position for reading the file

  logger.debug('----------DEBUG MODE START----------')

  f = open(args.file, 'r')
  f0 = open("t0.txt", 'w+')
  f1 = open("t1.txt", 'w+')
  f2 = open("t2.txt", 'w+')

  parse_file(f, f1)

  files_not_eq = True
  while (files_not_eq):
    parse_file(f1, f0)
    parse_file(f2, f1)
    parse_file(f0, f2)
    files_not_eq = parse_file_eq(f1, f2)

  f.close()
  f0.close()
  f1.close()
  f2.close()
  logger.debug('----------DEBUG MODE END------------')
  logger.info(total)

if __name__ == "__main__":
  # Get length of first line before starting
  f = open(args.file, 'r')
  line_len = len(f.readline().rstrip())
  f.close()
  main()