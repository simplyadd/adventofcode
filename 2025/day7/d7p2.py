import sys
sys.path.append('../../')
from parser import *

def main():
  stack = []
  temps = []  # temporary list of stack numbers
  total = 0

  f = open(args.file, 'r')
  l = f.readline()
  stack.append(l.index('S'))

  # Counts the number of possible paths per new splitter
  count = [0] * len(l.strip())
  count[stack[0]] = 1

  for l in f:
    logger.debug(''.join(f'{h:X}' for h in count))
    line = list(l.strip())

    i = 0
    elem = stack[i]

    while (stack):
      if (line[elem] == '^'):
        left  = elem-1
        right = elem+1
        count[left]  += count[elem]
        count[right] += count[elem]
        count[elem]   = 0

        temps.append(left)
        temps.append(right)
        stack.pop(i)
        i -= 1
      i += 1
      if (i < len(stack)):
        elem = stack[i]
      else:
        break

    if (temps):
      stack.extend(temps)
      stack = list(set(stack))
    temps = []

  for i in count:
    total += i
  logger.info(f'{total} \t{format(total, ',d')}')

if __name__ == "__main__":
  main()