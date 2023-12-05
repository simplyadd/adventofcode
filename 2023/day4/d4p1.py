import re
import sys

def main():
  try:
    input = open(sys.argv[1], 'r')
  except:
    input = open('test1.txt', 'r')

  sum = 0
  for line in input:
    points = 0

    winStart = re.search(r':', line).start()
    winEnd = re.search(r'\|', line).start()

    winList = re.findall(r'\d+', line[winStart:winEnd])
    numList = re.findall(r'\d+', line[winEnd:])
    for num in numList:
      if num in winList:
        if points == 0:
          points = 1
          continue
        points *= 2
    sum += points          
  
  print(sum)
  input.close()


if __name__ == "__main__":
  main()
    