import sys

cnt0 = 0

def convertRange(n: int) -> int:
  global cnt0

  '''Convert to be within range 0-99'''
  if n > 99:
    cnt0 += (n // 100)
    n %= 100
  return n

def main():
  global cnt0
  dial = 50

  try:
    input = open(sys.argv[1], 'r')
  except:
    input = open('input.txt', 'r')

  for line in input:
    d = line[0]                     # direction
    n = convertRange(int(line[1:])) # number of clicks

    temp = (dial + n) if (d == 'R') else (dial - n)

    if (temp < 0):
      cc = convertRange(abs(temp))  #counter-clockwise rotation
      if ((cc != 0) and (dial != 0)):
        cnt0 += 1
      dial = 100 - cc
    elif (temp == 0):
      dial = 0
      cnt0 += 1
    else:
      dial = convertRange(temp)

    if DEBUG_MODE:
      print(line.rstrip(), '\t', temp, '\t', dial, '\t', cnt0)
  input.close()
  print(cnt0)

if __name__ == "__main__":
  DEBUG_MODE = 1 if (sys.argv[-1]=='DEBUG') else 0
  main()