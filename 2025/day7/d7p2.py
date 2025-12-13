import sys
sys.path.append('../../')
from parser import *

def main():
  stack = []
  temps = []
  total = 0

  f = open(args.file, 'r')
  l = f.readline()
  stack.append(l.index('S'))

  current_splits = [0] * len(l.rstrip())
  line_splits = current_splits.copy()

  for l in f:
    line = list(l.strip())

    i = 0
    elem = stack[i]

    logger.debug(f'{''.join(str(i) for i in current_splits)} \t{total}')
    while (stack):
      if (line[elem] == '^'):
        left, right = elem-1, elem+1
        if ((current_splits[left] == 0) or (current_splits[right] == 0)):
          line_splits[left]  = 1
          line_splits[elem]  = 0
          line_splits[right] = 1
          temps.append(left)
          temps.append(right)
          stack.pop(i)
          total += 1
          i -= 1
      i += 1
      if (i < len(stack)):
        elem = stack[i]
      else:
        break

    if (temps):
      stack.extend(temps)
      stack = list(set(stack))

    line_splits = current_splits.copy()
    temps = []
  logger.info(total)

if __name__ == "__main__":
  main()