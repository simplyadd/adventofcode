import sys
from itertools import islice

def main():
    letters = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    score = 0
    temp = 0              
    with open("input.txt") as fp:
        while True:
            next_3_lines = list(islice(fp, 3))
            #line = fp.readline()

            if next_3_lines:
                line1 = next_3_lines[0]
                line2 = next_3_lines[1]
                line3 = next_3_lines[2]
                print(line1, line2, line3)

            i=0
            for x in line1:
                for y in line2:
                    for z in line3:
                        if (x==y) & (y==z) & (i==0):
                            temp = letters.index(str(x))
                            score += temp
                            print(x) 
                            i=1
                                
            if not next_3_lines:
                break
    print(score-temp)    
    fp.close()

if __name__ == "__main__":
    main()