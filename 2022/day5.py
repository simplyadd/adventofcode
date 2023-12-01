import sys

def main():
    count=0
    with open("input.txt") as fp:
        while True:
            line = fp.readline()
            

            #find first number to only transpose until that line
            checked = can_convert_to_int(line[1])
            if not checked:
                count += 1

            #lis = [x.replace('\n', '').split('[') for x in fp]

            #print(lis)
            #print(lis.T)
            print(count)
            if not line:
                break
    print(count)
    fp.close()

def can_convert_to_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()