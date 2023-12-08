import sys
from collections import Counter

handsList = {
  5: [],
  4: [],
  6: [],
  3: [],
  2: [],
  1: [],
  0: []
}

class Hand:
  __slots__ = ('cards', 'bid')
  def __init__(self, cards: str, bid: int):
    self.cards = cards
    self.bid = bid

  
def addToRank(type: int, cards: str, bid: str):
  global handsList
  listLen = len(handsList[type])
  bid  = int(bid)
  if listLen == 0:
    handsList[type].append(Hand(cards, bid))
    return
  
  i, j = 0, 0
  #get starting index
  if cards[0].isalpha() is True:
    i = 0
  elif int(cards[0]) > 5:
    i = listLen/2
  else:
    i = -1

  
  while True:
    x = getNum(cards[j])
    y = getNum(handsList[type][i].cards[j])
    try:
      y0 = getNum(handsList[type][i-1].cards[j])
    except:
      y0 = -1
    try:
      y2 = getNum(handsList[type][i+1].cards[j])
    except:
      y2 = 15


    if x > y:
      if (i == 0) | (x < y0):
        handsList[type].insert(i, Hand(cards, bid))
        break
      else:
        i -= 1
        continue


    if x < y:
      if (i == listLen-1) | (x > y2):
        handsList[type].insert(i, Hand(cards, bid))
        break
      else:
        i += 1
        continue


    if x == y:
      if listLen > 1:
        if ((i==0) & (x>y2)) | ((i==listLen-1) & (x<y0)):
          #compare j
          if compCards(cards, handsList[type][i].cards) is True:
            handsList[type].insert(i, Hand(cards, bid))
          else:
            try:
              handsList[type].insert(i+1, Hand(cards, bid))
            except:
              handsList[type].append(Hand(cards, bid))
          break

        if (x==y0) | (x==y2):
          #compare j
          if compCards(cards, handsList[type][i].cards) is True:
            i -= 1
          else:
            i += 1
          continue

      else:
        if compCards(cards, handsList[type][i].cards) is True:
          handsList[type].insert(i, Hand(cards, bid))
        else:
          handsList[type].append(Hand(cards, bid))
        break


def compCards(cardsLine: str, cardsDict: str) -> bool:
  for i in range(1, 6):
    x = getNum(cardsLine[i])
    y = getNum(cardsDict[i])

    if x > y:
      return True
    elif x < y:
      return False
    else:
      continue
  return True


def getNum(c: str):
  cardNum = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10
  }
  return int(c) if c.isnumeric() else cardNum[c]


def main():
  cnt = 0

  try:
    input = open(sys.argv[1], 'r')
  except:
    input = open('test1.txt', 'r')

  for line in input:
    cnt += 1
    cards, bid = line.rstrip().split(' ')
    #print(cards, bid)
    
    d = Counter(cards)
    dMaxCnt = max(d.values())
    dLength = len(d)
    #print(dMaxCnt, dLength)

    match dMaxCnt:
      case 5:
        #re.search(r'(.)\1{4}', line)
        addToRank(5, cards, bid)
      case 4:
        addToRank(4, cards, bid)
      case 3:
        if dLength == 2:
          #print('fullHouse')
          addToRank(6, cards, bid)
        else:
          #print('threeOfAKind')
          addToRank(3, cards, bid)
      case 2:
        if dLength == 3:
          #print('twoPair')
          addToRank(2, cards, bid)
        else:
          #print('onePair')
          addToRank(1, cards, bid)
      case 1:
        #print('highCard')
        addToRank(0, cards, bid)
      case _:
        print('Unexpected Err')
  
  input.close()
  global handsList
  res = 0
  for type, hands in handsList.items():
    for i in hands:
      print(type, i.cards, i.bid)
      res += cnt * i.bid
      cnt -= 1
      print(cnt, res)
  
  print(res)

if __name__ == "__main__":
  main()
    