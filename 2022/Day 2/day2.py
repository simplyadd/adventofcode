import sys

def main():
    score = 0
    newScore = 0
    with open("input.txt") as fp:
        while True:
            line = fp.readline()

            if(line ==""):
                break
            abc = line[0]
            xyz = line[2]

            if(xyz == "X"):
                score += 1
                if(abc == "C"):
                    score += 6
                    newScore += 2
                elif(abc == "A"):
                    score += 3
                    newScore += 3
                else:
                    newScore += 1
            elif(xyz == "Y"):
                score += 2
                newScore += 3
                if(abc == "A"):
                    score += 6
                    newScore += 1
                elif(abc == "B"):
                    score += 3
                    newScore += 2
                else:
                    newScore += 3
            elif(xyz == "Z"):
                score += 3
                newScore += 6
                if(abc == "B"):
                    score += 6
                    newScore += 3
                elif(abc == "C"):
                    score += 3
                    newScore += 1
                else:
                    newScore += 2
            
    print("Total Score:", score)
    print("New Score:", newScore)
    fp.close()

if __name__ == "__main__":
    main()