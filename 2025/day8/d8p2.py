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

CID = -1   # Circuit ID
class Circuit:
  def __init__(self):
    global CID
    CID += 1
    self.cid = CID
    self.cnt = 0
    self.lst = []
    self.prev = None
    self.next = None

  def __repr__(self):
    return f'ID {self.cid}'

  def add_circuit(self, new_circuit):
    self.prev = new_circuit
    new_circuit.next = self

  def add_junction(self, junction : Junction):
    self.cnt += 1
    self.lst.append(junction)
    junction.circuit = self

  def merge_circuit(self, junction : Junction):
    self.cnt += junction.circuit.cnt
    self.lst.extend(junction.circuit.lst)
    # Delete junction in the doubly linked list.
    if junction.circuit.prev is not None:
      junction.circuit.prev.next = junction.circuit.next
    if junction.circuit.next is not None:
      junction.circuit.next.prev = junction.circuit.prev
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

  circuits  = Circuit()
  distance  = []   # Distance between junctions
  junctions = []   # Array of Junction classes
  last_xcon = 0    # Product of X Coordinates of the last connection

  # Get all distances between points
  for line in f:
    x, y, z = re.findall(r'\d+', line)
    j2 = Junction([int(x), int(y), int(z)])
    for j1 in junctions:
      d = get_distance(j1.pos, j2.pos)
      distance.append([d, j1, j2])
    junctions.append(j2)

  # Group junctions closest to each other into circuits
  distance.sort()
  for i in range(len(distance)):
    j1 = distance[i][1]
    j2 = distance[i][2]
    if (j1.circuit is None) and (j2.circuit is None):
      circuit = Circuit()
      circuit.add_junction(j1)
      circuit.add_junction(j2)
      circuits.add_circuit(circuit)
      circuits = circuit  # circuit is the new head of circuits
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
    last_xcon = j1.pos[0] * j2.pos[0]

  f.close()
  logger.info(last_xcon)

if __name__ == "__main__":
  main()