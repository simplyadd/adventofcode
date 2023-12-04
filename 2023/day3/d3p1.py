import re
import sys

threeLines = ['', '', '']
sum = 0


def addCheckedPn(line: str, i: int, number: int) -> bool:
    try:
        c = line[i]
        
        global sum
        global count
        if c == '.':
            return False
        elif c.isnumeric() is True:
            return False
        else:
            sum += number
            return True
    except:
        return False


def readLines(i: int):
    if i == 1:
        prevLine = threeLines[i-1]
        currLine = threeLines[i]
        nextLine = threeLines[i+1]
    else:
        prevLine = threeLines[i-1]
        currLine = threeLines[i]
        nextLine = ''

    for number in re.finditer(r'\d+', currLine):
        lastIndex = len(currLine)-1
        start = number.start()
        end = number.end()
        number = int(number.group())
    
        if start > 0:
            start -= 1
            if addCheckedPn(currLine, start, number) is True:
                continue
        if end < lastIndex:
            if addCheckedPn(currLine, end, number) is True:
                continue
            end += 1
        for i in range(start, end):
            if addCheckedPn(prevLine, i, number) is True:
                break
            if addCheckedPn(nextLine, i, number) is True:
                break


def main():
    global count
    global threeLines

    try:
        input = open(sys.argv[1], 'r')
    except:
        input = open('test1.txt', 'r')
    
    for line in input:
        threeLines.append(line)
        threeLines.pop(0)
        
        #use threeLines[1] as current Line
        readLines(1)

    #for last line (threeLines[2])
    readLines(2)

    print(sum)
    input.close()


if __name__ == "__main__":
    main()
    