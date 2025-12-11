import sys
sys.path.append('../../')
from parser import *

def main():
  '''Print sum of highest "joltage" received for each power bank.'''

  sum = 0
  input = open(args.file, 'r')

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
    logger.debug(int(num))

  input.close()

  if (args.file == 'test.txt'): logger.info(f'Test Passed: {sum == 3121910778619}')
  else: logger.info(sum)

if __name__ == "__main__":
  main()