import re
import sys
from itertools import islice


def checkIfSymbol(line: str, i: int) -> bool:
    try:
        c = line[i]

        if c == '.':
            return False
        elif c.isnumeric() is True:
            return False
        else:
            #print(' Tis the char: ' + c)
            return True
    except:
        return False


def main():
    sum = 0
    threeLines = ['', '', '']

    try:
        input = open(sys.argv[1], 'r')
    except:
        input = open('test1.txt', 'r')
    
    for line in input:
        threeLines.append(line)
        threeLines.pop(0)
        
        prevLine = threeLines[0]
        currLine = threeLines[1]
        nextLine = threeLines[2]
        lastIndex = len(line)-1

        for number in re.finditer(r'\d+', currLine):
            start = number.start()
            end = number.end()
            number = int(number.group())

            #check before num
            if start > 0:
                start -= 1
                if checkIfSymbol(currLine, start) is True:
                    sum += number
                    continue
            #check after num
            if end < lastIndex:
                if checkIfSymbol(currLine, end) is True:
                    sum += number
                    continue
                end += 1
            #check previous and next lines
            for i in range(start, end):
                if checkIfSymbol(prevLine, i) is True:
                    sum += number
                    break
                if checkIfSymbol(nextLine, i) is True:
                    sum += number
                    break

    lastLine = threeLines[2]
    for number in re.finditer(r'\d+', lastLine):
        start = number.start()
        end = number.end()
        number = int(number.group())

        #check before num
        if start > 0:
            start -= 1
            if checkIfSymbol(lastLine, start) is True:
                sum += number
                continue
        #check after num
        if end < len(lastLine)-1:
            if checkIfSymbol(lastLine, end) is True:
                sum += number
                continue
            end += 1
        #check previous line
        for i in range(start, end):
            if checkIfSymbol(threeLines[1], i) is True:
                sum += number
                break

    print(sum)
    input.close()


if __name__ == "__main__":
    main()
    