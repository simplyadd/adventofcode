import sys
from collections import Counter

handsList = {
  5: [], #five of a kind
  4: [], #four of a kind
  6: [], #full house
  3: [], #three of a kind
  2: [], #two pair
  1: [], #one pair
  0: []  #high card
}

class Hand:
  __slots__ = ('cards', 'bid')
  def __init__(self, cards: str, bid: int):
    self.cards = cards
    self.bid = bid

  
def addToRank(type: int, cards: str, bid: str):
  global handsList
  bid = int(bid)
  listLen = len(handsList[type])
  if listLen == 0:
    handsList[type].append(Hand(cards, bid))
    return
  
  i, j = 0, 0
  if cards[0].isalpha() is True:
    i = 0
  else:
    i = int(listLen/2)
  
  while True:
    x = getNum(cards[j])
    y = getNum(handsList[type][i].cards[j])
    try:
      y0 = getNum(handsList[type][i-1].cards[j])
    except:
      y0 = 15
    try:
      y2 = getNum(handsList[type][i+1].cards[j])
    except:
      y2 = -1


    if x > y:
      if (i == 0) | (x < y0):
        insertBefore(type, i, cards, bid)
        break
      else:
        i -= 1
        continue

    if x < y:
      if (i == listLen-1) | (x > y2):
        insertAfter(type, i, cards, bid)
        break
      else:
        i += 1
        continue

    if x == y:
      compxy = compCards(cards, handsList[type][i].cards)
      if listLen > 1:
        if (compxy is True):  
          if (x==y0):
            compxy0 = compCards(cards, handsList[type][i-1].cards)
            if compxy0 is False:
              insertBefore(type, i, cards, bid)
              break
            else:
              i -= 1
              continue
          if (x < y0) | (i==0):
            insertBefore(type, i, cards, bid)
            break

        if (compxy is False):
          if (x==y2):
            compxy2= compCards(cards, handsList[type][i+1].cards)
            if compxy2 is True:
              insertAfter(type, i, cards, bid)
              break
            else:
              i += 1
              continue 
          if (x > y2):
            insertAfter(type, i, cards, bid)
            break
      else:
        if compxy is True:
          insertBefore(type, i, cards, bid)
        else:
          insertAfter(type, i, cards, bid)
        break

#compare cards with the same start
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

#get equivalent Rank of Ace, King, Queen, Jack, Ten
def getNum(c: str):
  cardNum = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10
  }
  return int(c) if c.isnumeric() else cardNum[c]

#insert cards and bid in the list based on order
def insertBefore(type: int, i: int, cards: str, bid: int):
  global handsList
  handsList[type].insert(i, Hand(cards, bid))
def insertAfter(type: int, i: int, cards: str, bid: int):
  global handsList
  try:
    handsList[type].insert(i+1, Hand(cards, bid))
  except:
    handsList[type].append(Hand(cards, bid)) 


def main():
  cnt = 0

  try:
    input = open(sys.argv[1], 'r')
  except:
    input = open('input.txt', 'r')

  for line in input:
    cnt += 1
    cards, bid = line.rstrip().split(' ')
    #print(cnt, cards, bid)
    
    d = Counter(cards)
    dMaxCnt = max(d.values())
    dLength = len(d)

    match dMaxCnt:
      case 5:
        addToRank(5, cards, bid)
      
      case 4:
        addToRank(4, cards, bid)
      
      case 3:
        if dLength == 2:
          addToRank(6, cards, bid)
        else:
          addToRank(3, cards, bid)
      
      case 2:
        if dLength == 3:
          addToRank(2, cards, bid)
        else:
          addToRank(1, cards, bid)
      
      case 1:
        addToRank(0, cards, bid)
      
      case _:
        print('Unexpected Err')
  
  input.close()
  global handsList
  res = 0
  for type, hands in handsList.items():
    for i in hands:
      res += cnt * i.bid
      cnt -= 1
  
  print(res)


if __name__ == "__main__":
  main()
    