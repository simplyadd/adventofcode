import re
import sys

seeds = []

class Seed:
  def __init__(self, seed: int, maxRange: int):
    self.seed = seed
    self.maxRange = maxRange

def main():
  global seeds
  try:
    input = open(sys.argv[1], 'r')
  except:
    input = open('test1.txt', 'r')
  
  #get seeds from first line
  line = input.readline()
  line = [int(v) for v in re.findall(r'\d+', line)]
  for i in range(0, len(line), 2):
    seeds.append(Seed(line[i], line[i+1]))

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
          #convert from (fr) this number
          fr = getattr(seed, item[-2])
        except:
          setattr(seed, item[-2], getattr(seed, item[-3]))
          fr = getattr(seed, item[-2])

        if fr >= mapVals[1]:
          itemRange = mapVals[1] + mapVals[2]
          if fr < itemRange:
            v = mapVals[0] + (fr - mapVals[1])
            setattr(seed, item[-1], v)
          continue
        
        maxSeed = fr + seed.maxRange
        if maxSeed >= mapVals[1]:
          #get start of newSeed/end of currSeed
          diff = mapVals[1] - fr
          newMaxRange = seed.maxRange - diff
          newSeed = fr + diff

          seeds.append(Seed(newSeed, newMaxRange))
          seed.maxRange = diff #limit max of currSeed so no duplicates
          setattr(seeds[-1], item[-2], newSeed)
        else:
          continue

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
    