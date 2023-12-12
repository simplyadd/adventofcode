import re
import sys

line1 = ''
nodes = []
stepCnt, cnt = 0, 0

class Node:
  __slots__ = ('value', 'left', 'right')
  def __init__(self, value: str, left: str, right: str):
    self.value = value
    self.left = left
    self.right = right


def searchNode(step: str) -> str:
  global nodes, stepCnt, cnt
  for node in nodes:
    if step == 'ZZZ':
        return step
    if step == node.value:
      if cnt == len(line1)-1:
        cnt = 0
      
      dest = line1[cnt]
      if dest == 'L':
        step = node.left
      if dest == 'R':
        step = node.right

      #print(stepCnt, step, dest)
      cnt += 1
      stepCnt += 1
      return step

def main():
  global nodes, stepCnt, cnt, line1
  nodesVal = []
  step = 'AAA'
  
  try:
    input = open(sys.argv[1], 'r')
  except:
    input = open('input.txt', 'r')

  line1 = input.readline()

  for line in input:
    try:
      value, left, right = re.findall(r'[A-Z]+', line)
    except:
      continue
    
    nodes.append(Node(value, left, right))
    nodesVal.append(value)

    if step in nodesVal:
      step = searchNode(step)
    elif step == 'ZZZ':
      break
    else:
      continue
  input.close()

  while (step != 'ZZZ'):
    step = searchNode(step)

  print(stepCnt)

if __name__ == "__main__":
  main()
    