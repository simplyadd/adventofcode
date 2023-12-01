import sys

def main():
    letters = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    score = 0              
    comp1 = ""
    comp2 = ""
    with open("input.txt") as fp:
        while True:
            line = fp.readline()
            size = len(line)
            halfSize= int(size/2)

            comp1 = line[0:halfSize]
            comp2 = line[halfSize:size]

            #print(comp1, comp2)

            i=0
            for x in comp1:
                for y in comp2:
                    if i==0:
                        if x == y:
                            score += letters.index(str(x))
                            #print(x) 
                            i=1

            if not line:
                break
    print(score)    
    fp.close()

if __name__ == "__main__":
    main()