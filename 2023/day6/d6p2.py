import sys

def getNum(line: str) -> int:
  num = ''
  for c in line:
    if c.isnumeric() is True:
      num += c
  return int(num)

def main():
  try:
    input = open(sys.argv[1], 'r')
  except:
    input = open('input.txt', 'r')

  t = input.readline()
  d = input.readline()
  input.close()

  t = getNum(t)
  d = getNum(d)
  
  for ms in range(t):
    mm = (t-ms) * ms

    if mm > d:
      #print(ms, t-ms) #end, start
      #end-start+1 to get range of wins
      totalWins = t+1 - (2*ms)
      print(totalWins)
      break

if __name__ == "__main__":
  main()
  