import sys


def get_input(filename):
    f = open(filename, "r")
    input = []
    for line in f.readlines():
        input.append(int(line))
    return input

def main():
    GOAL=2020
    print(f"Looking for: {str(GOAL)}")
    input = get_input("input.txt")
    input.sort()
    print(str(input))

    i = 0
    j = 1
    k = 2
    c = len(input)
    found = False
    while(i < c):
        while(j < c):    
            while( k < c):        
                print(f"Doing: {str(i)} , {str(j)}, {str(k)}: Found : {str(input[i])} + {str(input[j])} + {str(input[k])} = {str(input[i] + input[j] + input[k])}")        
                if input[i] + input[j] + input[k] == GOAL:  
                    found = True
                    break
                k += 1   
            if found == True:
                break
            k = 0
            j += 1
            
        if found == True:
            break
        i += 1
        j = 0

    if found:        
        print(f"Doing: {str(i)} , {str(j)}, {str(k)}: Found : {str(input[i])} + {str(input[j])} + {str(input[k])} = {str(input[i] + input[j] + input[k])}")
        print(str(input[i]*input[j]*input[k]))
    else:
        print("Didn't find answer in input")


if __name__ == "__main__":
    main()