import sys

def convertRange(n: int) -> int:
  '''Convert to be within range 0-99'''
  if n > 99:
    n %= 100
  return n

def main():
  dial = 50
  cnt0 = 0

  try:
    input = open(sys.argv[1], 'r')
  except:
    input = open('input.txt', 'r')

  for line in input:
    d = line[0]                     # direction
    n = convertRange(int(line[1:])) # number of clicks

    temp = (dial + n) if (d == 'R') else (dial - n)

    if (temp < 0):
      dial = 100 - convertRange(abs(temp))
    else:
      dial = convertRange(temp)

    if (dial == 0):
      cnt0 += 1

    print(temp, '\t', dial)
  input.close()
  print(cnt0)

if __name__ == "__main__":
  main()