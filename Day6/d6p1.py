import sys
from functools import reduce

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