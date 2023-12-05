import re
import sys

def main():
  try:
    input = open(sys.argv[1], 'r')
  except:
    input = open('test1.txt', 'r')

  d = {}
  sum, cardN = 0, 0
  
  for line in input:
    cardN += 1
    d[cardN] = d.get(cardN, 0) + 1

    winStart = re.search(r':', line).start()
    winEnd = re.search(r'\|', line).start()

    winList = re.findall(r'\d+', line[winStart:winEnd])
    numList = re.findall(r'\d+', line[winEnd:])

    matchCnt = 0
    for num in numList:
      if num in winList:
          matchCnt += 1

    for i in range(matchCnt):
      d[cardN+i+1] = d.get(cardN+i+1, 0) + 1 * d[cardN]
    
  for v in d.values():
    sum += v

  print(sum)
  input.close()


if __name__ == "__main__":
  main()
    