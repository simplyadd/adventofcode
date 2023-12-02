# Day 1
# Get sum of calibration values in each line.
# The calibration value can be found by combining the first and last 
# digit (in that order) to form a single two-digit number.

def main():
    calVals = []
    firstDigit, lastDigit, sum = 0, 0, 0

    file1 = open('input.txt', 'r')

    while True:
        line = file1.readline()

        if not line:
            break
    
        for i in line:
            if i.isnumeric() == True:
                firstDigit = str(i)
                break
        for j in reversed(line):
            if j.isnumeric() == True:
                lastDigit = str(j)
                break
        #concat chars
        num = int(firstDigit + lastDigit)

        sum += num
        calVals.append(num)

    print(sum)
    file1.close()

if __name__ == "__main__":
    main()
    