import re
import sys

gearList = []
threeLines = ['', '', '']
sum = 0


class findGears:
    def __init__(self, start: int):
        global threeLines
        global sum
        global gearList
        self.start = start

        gearList = []
        try:
            prev = self.isAdjacent(threeLines[0], start)
            curr = self.isAdjacent(threeLines[1], start)
            next = self.isAdjacent(threeLines[2], start)
        except: #last line
            prev = self.isAdjacent(threeLines[0], start)
            curr = self.isAdjacent(threeLines[1], start)
            next = False

        if prev is True:
            self.getGears(threeLines[0], start)
        if curr is True:
            self.getGears(threeLines[1], start)
        if next is True:
            self.getGears(threeLines[2], start)

        if len(gearList) == 2:
            sum += gearList[0] * gearList[1]
    

    def isAdjacent(self, line: str, start: int) -> bool:
        for i in line[start-1:start+2]:
            if i.isnumeric() is True:
                return True
        return False
   

    def getGears(self, line: str, start: int):
        for gear in re.finditer(r'\d+', line[start-3:start+4]): 
            startGear = gear.start() + start-3
            endGear = gear.end() + start-3
            
            if ((startGear <= start+1) & (endGear >= start)):
                gear = gear.group() 
                gearPn = int(re.search(r'\d+', gear).group())
                gearList.append(gearPn)


def main():
    global threeLines

    try:
        input = open(sys.argv[1], 'r')
    except:
        input = open('test1.txt', 'r')
    
    for line in input:
        threeLines.append(line)
        threeLines.pop(0)
        
        #use threeLines[1] as current Line
        currLine = threeLines[1]
        for gearSymbol in re.finditer(r'\*', currLine):
            start = gearSymbol.start()
            findGears(start)

    #for last line
    threeLines.pop(0)
    findGears(start)

    print(sum)
    input.close()


if __name__ == "__main__":
    main()
