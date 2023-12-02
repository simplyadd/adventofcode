def getDigit(line: str) -> str:
    for c in line:
        if c.isnumeric() == True:
            return c


def main():
    firstDigit, lastDigit, sum = 0, 0, 0

    file1 = open('input.txt', 'r')
    while True:
        line = file1.readline()

        if not line:
            break
        
        firstDigit = getDigit(line)
        lastDigit = getDigit(reversed(line))
        
        #concat chars
        num = int(firstDigit + lastDigit)

        sum += num
    print(sum)
    file1.close()


if __name__ == "__main__":
    main()
    