import re

def main():
    sum = 0
    toMatch = {'red': 12, 
               'green': 13,
               'blue': 14}
    
    file1 = open('input.txt', 'r')
    while True:
        line = file1.readline()
        
        if not line:
            break
        
        flag=0
        d= {'red': 0, 
            'green': 0,
            'blue': 0}
        gameID = int(re.search(r'\d+', line).group())
        for match in re.finditer(r'\d+ (red|green|blue)', line):
            match = match.group()
            count = int(re.search(r'\d+', match).group())
            color = re.search(r'red|green|blue', match).group()
            if d[color] < count:
                d[color] = count
            if d[color] > toMatch[color]:
                flag=1
                break 

        #if match, add gameID
        if flag==0:
            sum += gameID
        #print('Game ' + str(gameID) + ': ' + str(flag))

    print(sum)
    file1.close()


if __name__ == "__main__":
    main()
    