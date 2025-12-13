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

  for l in f:
    line = list(l.strip())

    i = 0
    elem = stack[i]

    while (stack):
      if (line[elem] == '^'):
        temps.append(elem-1)
        temps.append(elem+1)
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
    temps = []
  logger.info(total)

if __name__ == "__main__":
  main()