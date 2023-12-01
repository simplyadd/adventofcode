import sys

def main():
    totalCal =[]
    sum = 0
    with open("input.txt") as fp:
        while True:
            line = fp.readline()
            line2 = line.replace("\n", "")
            if( line2 == "" ):
                #append to list
                totalCal.append(sum)
                sum = 0 
            else:
                sum += int(line2)
                
            if not line:
                break
    
    #Find biggest value
    print("Max total Caloriess: ", max(totalCal))

    totalCal.sort(reverse=True)
    print(totalCal[0] + totalCal[1] + totalCal[2])
    fp.close()

if __name__ == "__main__":
    main()