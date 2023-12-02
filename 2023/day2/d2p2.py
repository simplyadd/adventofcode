import re
import sys

def main():
    sum = 0
    
    try:
        input = open(sys.argv[1], 'r')
    except:
        input = open('test1.txt', 'r')
    
    while True:
        minPower = 1
        line = input.readline()
        
        if not line:
            break

        d= {'red': 0, 
            'green': 0,
            'blue': 0}
        for match in re.finditer(r'\d+ (red|green|blue)', line):
            match = match.group()
            count = int(re.search(r'\d+', match).group())
            color = re.search(r'red|green|blue', match).group()
            if d[color] < count:
                d[color] = count
        for v in d.values():
            minPower *= v
        sum += minPower

    print(sum)
    input.close()


if __name__ == "__main__":
    main()
    