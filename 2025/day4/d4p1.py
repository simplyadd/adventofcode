import re
import sys

threeLines = ['', '', '']
total = 0


def check_if_accessible(start: int) -> bool:
  global threeLines
  try:
    adjacent = 0
    adjacent += count_adjacent(threeLines[0], start)
    adjacent += count_adjacent(threeLines[1], start)
    adjacent += count_adjacent(threeLines[2], start)
  except: # For last line
    adjacent = 0
    adjacent += count_adjacent(threeLines[0], start)
    adjacent += count_adjacent(threeLines[1], start)
  return True if (adjacent-1 < 4) else False


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
    total += 1 if (found) else 0
  return


def find_rolls_dbg(line: str):
  global total
  test  = ''
  for i, c in enumerate(line):
    if (c == '@'):
      found = check_if_accessible(i)
      total += 1 if (found) else 0
    else:
      found = False
    test += 'x' if (found) else line[i]
  print(test)
  return


def main():
  global threeLines
  global total

  try:
    input = open(sys.argv[1], 'r')
  except:
    input = open('input.txt', 'r')

  if DEBUG_MODE:
    print('----------DEBUG MODE START----------\n')

  for line in input:
    threeLines.append(line.rstrip()) # Add new index
    threeLines.pop(0)                # Keep length at 3
    curr = threeLines[1]

    # Iterates through the whole string when debugging
    find_rolls_dbg(curr) if DEBUG_MODE else find_rolls(curr)

  # For last line
  threeLines.pop(0)
  find_rolls_dbg(curr) if DEBUG_MODE else find_rolls(curr)

  input.close()
  if DEBUG_MODE:
    print('----------DEBUG MODE END------------\n')
  print(total)

if __name__ == "__main__":
  DEBUG_MODE = 1 if (sys.argv[-1]=='DEBUG') else 0

  # Get length of first line before starting
  try:
    input = open(sys.argv[1], 'r')
  except:
    input = open('input.txt', 'r')
  line_len = len(input.readline().rstrip())
  input.close()
  main()