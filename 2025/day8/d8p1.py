import math
import re
import sys
sys.path.append('../../')
from parser import *

class Junction:
  def __init__(self, pos: list):
    self.pos     = pos
    self.circuit = None

  def __repr__(self):
    return f'{self.circuit}: {self.pos}'

  def __gt__(self, other):
    return self.pos > other.pos

CID = 0   # Circuit ID
class Circuit:
  def __init__(self):
    global CID
    CID += 1
    self.cid = CID
    self.cnt = 0
    self.lst = []

  def __repr__(self):
    return f'ID {self.cid}'

  def add_junction(self, junction : Junction):
    self.cnt += 1
    self.lst.append(junction)
    junction.circuit = self

  def merge_circuit(self, junction : Junction):
    self.cnt += junction.circuit.cnt
    self.lst.extend(junction.circuit.lst)
    junction.circuit.cnt = 0
    junction.circuit.lst = []

    # All junctions within the circuit should have the same circuit.
    for junc in self.lst:
      if junc.circuit.cid != self.cid:
        junc.circuit = self

def get_distance(p1 : list, p2 : list) -> int:
  x = (p2[0]-p1[0]) ** 2
  y = (p2[1]-p1[1]) ** 2
  z = (p2[2]-p1[2]) ** 2
  d = math.isqrt(x + y + z)
  return d

def main():
  f = open(args.file, 'r')

  circuits  = []   # Array of Circuit classes
  distance  = []   # Distance between junctions
  junctions = []   # Array of Junction classes

  # Get all distances between points
  for line in f:
    x, y, z = re.findall(r'\d+', line)
    j2 = Junction([int(x), int(y), int(z)])
    for j1 in junctions:
      d = get_distance(j1.pos, j2.pos)
      distance.append([d, j1, j2])
    junctions.append(j2)

  distance.sort()
  r = 10 if (args.file=='test.txt') else 1000
  for i in range(r):
    j1 = distance[i][1]
    j2 = distance[i][2]
    if (j1.circuit is None) and (j2.circuit is None):
      circuit = Circuit()
      circuit.add_junction(j1)
      circuit.add_junction(j2)
      circuits.append(circuit)
    elif j1.circuit is None:
      circuit = j2.circuit
      circuit.add_junction(j1)
    elif j2.circuit is None:
      circuit = j1.circuit
      circuit.add_junction(j2)
    elif j1.circuit.cid == j2.circuit.cid:
      continue
    else:
      circuit = j1.circuit
      circuit.merge_circuit(j2)

  top3 = [0, 0, 0]
  for circuit in circuits:
    count = circuit.cnt
    if count < top3[0]:
      continue
    elif count > top3[2]:
      top3.append(circuit.cnt)
      top3.pop(0)
    elif count > top3[1]:
      top3[0] = top3[1]
      top3[1] = count
    else: # count > top3[0]
      top3[0] = count

  f.close()
  product = top3[0] * top3[1] * top3[2]
  logger.info(product)

if __name__ == "__main__":
  main()