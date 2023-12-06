import re
import sys

class Seed:
  def __init__(self, seed: int):
    self.seed = seed

def main():
  seeds = []
  
  try:
    input = open(sys.argv[1], 'r')
  except:
    input = open('input.txt', 'r')
  
  #get seeds from first line
  line = input.readline()
  for seed in re.finditer(r'\d+', line):
    seed = int(seed.group())
    seeds.append(Seed(seed))

  item = ['seed'] #item conversion name to save to class Seed
  for line in input:
    if item[-1] in line:
      item.append(re.search(r'[a-z]+', line[len(item[-1])+4:]).group())
      continue
    elif line == '\n':
      continue
    else:
      #mapVals = [dest, source, range]
      mapVals = [int(v) for v in re.findall(r'\d+', line)]

      for seed in seeds:
        try:
          fr = getattr(seed, item[-2])
        except:
          setattr(seed, item[-2], getattr(seed, item[-3]))
          fr = getattr(seed, item[-2])

        if fr >= mapVals[1]:
          itemRange = mapVals[1] + mapVals[2]
          if fr < itemRange:
            v = mapVals[0] + (fr - mapVals[1])
            setattr(seed, item[-1], v)
        else:
          continue

  #for seed in seeds:
  #    setattr(seed, 'location', 0)
  res = []
  for seed in seeds:
    try:
      res.append(seed.location)
    except:
      res.append(seed.humidity)
  print(min(res))
  input.close()

if __name__ == "__main__":
  main()
    