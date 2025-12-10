import re
import sys
sys.path.append('../../')
from parser import *

def get_product(l : list):
  product = 1
  for elem in l[:-1]:
    product *= int(elem)
  return product

def get_sum(l : list):
  sum = 0
  for elem in l[:-1]:
    sum += int(elem)
  return sum

def main():
  rows = []
  total = 0

  with open(args.file, 'r') as f:
    lines = f.readlines()

  # Transpose file
  for l in lines:
    line = l.strip()
    rows.append(re.split(r'\s+', line))
  columns = list(zip(*rows))

  for col in columns:
    if col[-1] == '*':
      total += get_product(col)
    elif col[-1] == '+':
      total += get_sum(col)

  logger.debug(rows)
  logger.debug(columns)
  logger.info(total)

if __name__ == "__main__":
  main()