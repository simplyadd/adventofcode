def getDigit(line: str) -> str:
    for c in line:
        if c.isnumeric() == True:
            return c


def main():
    firstDigit, lastDigit, sum = 0, 0, 0
    d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
         'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    file1 = open('test.txt', 'r')
    while True:
        line = file1.readline()

        if not line:
            break
        '''
        s = [key for key in d.keys() if(key in line)]
        print(s)
        '''
        for k, v in d.items():
            if k in line:
                line = line.replace(k, str(v))

        
        firstDigit = getDigit(line)
        lastDigit = getDigit(reversed(line))
        
        calVal = int(firstDigit + lastDigit)

        sum += calVal
    print(sum)
    file1.close()


if __name__ == "__main__":
    main()
    