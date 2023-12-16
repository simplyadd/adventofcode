import re
import sys

toExtrapolate = []

def predictVal(sequence: list):
  global toExtrapolate
  nextSeq = []  
  
  toExtrapolate.insert(0, sequence[0])

  for i in range(len(sequence)-2, -1, -1):
    diff = sequence[i+1] - sequence[i]
    nextSeq.insert(0, diff)

  nextSeqSet = list(set(nextSeq))
  if (len(nextSeqSet)==1) and (nextSeqSet[0]==0):
    return
  else:
    predictVal(nextSeq)


def main(): 
  global toExtrapolate
  sum, extrapolate = 0, 0

  try:
    input = open(sys.argv[1], 'r')
  except:
    input = open('input.txt', 'r')

  for line in input:
    toExtrapolate = []
    extrapolate = 0

    history = [int(i) for i in re.findall(r'[-]?\d+', line)]
    predictVal(history)

    for i in range(0, len(toExtrapolate)):
      extrapolate = toExtrapolate[i] - extrapolate
    sum += extrapolate

  input.close()
  print(sum)

if __name__ == "__main__":
  main()
    