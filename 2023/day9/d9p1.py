import re
import sys

extrapolate = 0

def predictVal(sequence: list):
  global extrapolate
  nextSeq = []  
  
  extrapolate += sequence[-1]

  for i in range(0, len(sequence)-1):
    diff = sequence[i+1] - sequence[i]
    nextSeq.append(diff)
  
  nextSeqSet = list(set(nextSeq))
  if (len(nextSeqSet)==1) and (nextSeqSet[0]==0):
    return
  else:
    predictVal(nextSeq)


def main(): 
  global extrapolate
  sum = 0

  try:
    input = open(sys.argv[1], 'r')
  except:
    input = open('input.txt', 'r')

  for line in input:
    extrapolate = 0
    history = [int(i) for i in re.findall(r'[-]?\d+', line)]
    predictVal(history)
    sum += extrapolate
  input.close()
  print(sum)

if __name__ == "__main__":
  main()
    