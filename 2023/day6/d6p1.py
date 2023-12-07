import re
import sys

def getNums(line: str) -> list:
  nums = [int(v) for v in re.findall(r'\d+', line)]
  return nums

def main():
  product = 1
  
  try:
    input = open(sys.argv[1], 'r')
  except:
    input = open('input.txt', 'r')

  ts = input.readline()
  ds = input.readline()
  input.close()

  ts = getNums(ts)
  ds = getNums(ds)
  
  
  for i, t in enumerate(ts):
    for ms in range(t):
      mm = (t-ms) * ms

      if mm > ds[i]:
        #print(ms, t-ms) #end, start
        #end-start+1 to get range of wins
        totalWins = t+1 - (2*ms)
        product *= totalWins
        break
  
  print(ts, ds)
  print(product)
  

if __name__ == "__main__":
  main()
    