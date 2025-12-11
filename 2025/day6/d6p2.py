import sys
sys.path.append('../../')
from parser import *

def get_product(nums : list):
  product = 1
  for num in nums:
    product *= int(num)
  return product

def get_sum(nums : list):
  sum = 0
  for num in nums:
    sum += int(num)
  return sum

def main():
  rows = []
  total = 0

  f = open(args.file, 'r')

  # Transpose file
  for line in f:
    rows.append(list(line))
  columns = list(zip(*rows))

  nums = []
  for col in reversed(columns):
    word = ''.join(col).strip()
    if word.isnumeric():
      nums.append(word)
    elif (word == ''):
      continue
    else:
      nums.append(word[:-1])
      if col[-1] == '*':
        total += get_product(nums)
      elif col[-1] == '+':
        total += get_sum(nums)
      logger.debug(f'total {col[-1]}= {nums} = {total}')
      nums = []
  logger.info(total)

if __name__ == "__main__":
  main()