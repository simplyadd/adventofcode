import re
import sys

def main():
  '''Print sum of highest "joltage" received for each power bank.'''

  sum = 0

  try:    input = open(sys.argv[1], 'r')
  except: input = open('input.txt', 'r')

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
  # when input file is test.txt
  if DEBUG_TEST: print(f'Test Passed: {sum == 357}')
  else: print(sum)

if __name__ == "__main__":
  DEBUG_TEST = 1 if (sys.argv[-1]=='DTEST') else 0
  main()