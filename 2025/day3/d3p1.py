import sys
sys.path.append('../../')
from parser import *

def main():
  '''Print sum of highest "joltage" received for each power bank.'''

  sum = 0
  input = open(args.file , 'r')

  for l in input:
    line = l.rstrip()
    nums = [int(c) for c in line]
    num1_max = max(nums)
    num1_ind = nums.index(num1_max)
    if (num1_ind == len(line)-1):
      num2_max = nums.pop(-1)
      num1_max = max(nums)
      num1_ind = nums.index(num1_max)
    else:
      num2_max = max(nums[num1_ind+1:])
    sum += num1_max * 10 + num2_max

  input.close()

  if (args.file == 'test.txt'): logger.info(f'Test Passed: {sum == 357}')
  else: logger.info(sum)

if __name__ == "__main__":
  main()