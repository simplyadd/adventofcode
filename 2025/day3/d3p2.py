import re
import sys

def main():
  '''Print sum of highest "joltage" received for each power bank.'''

  sum = 0

  try:    input = open(sys.argv[1], 'r')
  except: input = open('input.txt', 'r')

  for l in input:
    line = l.rstrip()
    inv = 11 # last indices not to check when getting the max
    num, max, ind = '', 0, -1

    while (len(num) != 12):
      for i in range(ind+1, len(line)-inv):
        n = int(line[i])
        if (n > max): max, temp = n, i
      num += str(max)
      max, ind = 0, temp
      inv -= 1
    sum += int(num)
    if DEBUG_MODE:
      print(int(num))

  input.close()
  # when input file is test.txt
  if DEBUG_TEST: print(f'Test Passed: {sum == 3121910778619}')
  else: print(f'\n{sum}')

if __name__ == "__main__":
  DEBUG_MODE = 1 if (sys.argv[-1]=='DEBUG') else 0
  DEBUG_TEST = 1 if (sys.argv[-1]=='DTEST') else 0
  main()