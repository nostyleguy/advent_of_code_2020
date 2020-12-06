import sys
from functools import reduce

def get_input(filename):
    f = open(filename, "r")
    input2 =[]
    input= [y.split('\n') for y in [x for x in f.read().split('\n\n')] ]
    for group in input:
        try:
            group.remove('')
        except:
            pass
        group2 = list(map(lambda x: [char for char in x], group))
        input2.append(group2)
    return input2

def main():  
    filename = sys.argv[1] if (len(sys.argv) > 1) else "input.txt"
    input=get_input(filename)
    unique_counts = list(map(lambda x: len(set(x[0]).intersection(*x)), input))
    total = reduce((lambda x,y: x + y), unique_counts)
    print(f"Total: {str(total)}")  
    
if __name__ == "__main__":
    main()