import re
import sys

nl = '\n'

class bcolors:
    MAGENTA = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_input(filename):
    f = open(filename, "r")
    return f.read().split('\n')

def get_seat(line):
    for f in line[:7]:
        if f == "F":
            print("front")
        else:
            print("back")

def divide(sequence, first,last):
    if len(sequence) == 0:
        #print(f"Sequence length 0: {str(sequence)} returning {str(first)}")
        return first


    if sequence[0] in ['F','L']:        
        new_first=first
        new_last=int(((last-first) / 2) + first)
        #print(f"Got {sequence[0]} Sequence {str(sequence)} First: {str(first)} Last: {str(last)} NFirst: {str(new_first)} NLast: {str(new_last)}")
        #return divide(sequence[1:], new_first, new_last)
    else:
        new_first=int(((last-first) / 2) + first + 1)
        new_last=last
        #print(f"Got {sequence[0]} Sequence {str(sequence)} First: {str(first)} Last: {str(last)} NFirst: {str(new_first)} NLast: {str(new_last)}")
        
    return divide(sequence[1:], new_first, new_last)

def do_it(x):
    return 8 * divide(x[:7],0,127)  + divide(x[7:], 0, 7)
def main():  
    filename = sys.argv[1] if (len(sys.argv) > 1) else "input.txt"
    input=get_input(filename)
    print(f"Max: {str(max(map(lambda x : (8 * divide(x[:7],0,127)  + divide(x[7:], 0, 7)) , input)))}")

    
if __name__ == "__main__":
    main()