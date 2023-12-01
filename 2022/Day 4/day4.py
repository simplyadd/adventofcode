import sys

def main():
    count=0
    with open("input.txt") as fp:
        while True:
            line = fp.readline()

            if line:
                pair1 = line.split(",")[0]
                pair2 = line.split(",")[1]

                pair1_1 = int(pair1.split("-")[0])
                pair1_2 = int(pair1.split("-")[1])
                pair2_1 = int(pair2.split("-")[0])
                pair2_2 = int(pair2.split("-")[1])

                if (pair1_1 >= pair2_1) & (pair1_2 <= pair2_2):
                    count += 1
                elif (pair2_1 >= pair1_1) & (pair2_2 <= pair1_2):
                    count +=1
            #print(pair1, pair2)

            if not line:
                break
    print(count)
    fp.close()

if __name__ == "__main__":
    main()