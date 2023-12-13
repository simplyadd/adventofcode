import re
import sys
import math

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
    if step.endswith('Z') is True:
        return step
    if step == node.value:
      if cnt == len(line1)-1:
        cnt = 0
      
      dest = line1[cnt]
      if dest == 'L':
        step = node.left
      if dest == 'R':
        step = node.right

      cnt += 1
      stepCnt += 1
      return step

def main():
  global nodes, stepCnt, line1
  step = ''
  firstSteps = []
  tempCnt = []
  
  try:
    input = open(sys.argv[1], 'r')
  except:
    #input = open('test3.txt', 'r')
    input = open('input.txt', 'r')

  line1 = input.readline()
  for line in input:
    try:
      value, left, right = re.findall(r'[A-Z0-9]+', line)
    except:
      continue
    
    nodes.append(Node(value, left, right))
    if value.endswith('A'):
      firstSteps.append(value)
  input.close()


  for firstStep in firstSteps:
    stepCnt = 0
    step = searchNode(firstStep)

    while (step.endswith('Z') is False):
      step = searchNode(step)
    tempCnt.append(stepCnt)

  print(math.lcm(*tempCnt))
  
if __name__ == "__main__":
  main()
    