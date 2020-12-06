import re
import sys
from functools import reduce

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
    return list(map(lambda x: x.replace('\n',''), f.read().split('\n\n')))

def process(g):
    return len(set([char for char in g]))

def main():  
    filename = sys.argv[1] if (len(sys.argv) > 1) else "input.txt"
    input=get_input(filename)
    group_scores = list(map(process, input))
    total = reduce((lambda x,y: x + y), group_scores)

    print(f"Total: {str(total)}")  

    
if __name__ == "__main__":
    main()