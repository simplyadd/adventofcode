import sys

def main():
    a, b, c, d = 0, 1, 2, 3
    count = 0
    
    with open("input.txt") as fp:
        input = fp.readline()

        for x in input:
            list = [input[a], input[b], input[c], input[d]]
            myset = set(list)
            
            if (count<len(input)-3) & (count>3):
                if len(myset) == 4:
                    print('first marker after character', d+1)
                    break
                if x in list:
                    a = count + list.index(x)
                    b = a+1
                    c = a+2
                    d = a+3
            count += 1
    fp.close()

if __name__ == "__main__":
    main()