import re

def main():
    firstDigit, lastDigit, sum = 0, 0, 0
    
    file1 = open('input.txt', 'r')
    while True:
        line = file1.readline()
        
        if not line:
            break
        
        x = re.findall('(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))', line)
        
        d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
            'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,}
        
        firstDigit = x[0]
        lastDigit = x[-1]
        
        if firstDigit in d.keys():
            firstDigit = d[firstDigit]
        if lastDigit in d.keys():
            lastDigit = d[lastDigit]
        
        calVal = int(str(firstDigit) + str(lastDigit))

        sum += calVal
    print(sum)
    file1.close()


if __name__ == "__main__":
    main()
    