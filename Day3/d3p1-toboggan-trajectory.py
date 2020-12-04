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
    input = []
    for line in f.readlines():
        input.append(line)
    return input

def get_trees_for_slope(data):

    input=data[0]
    RISE=data[1]
    RUN=data[2]

    print(f"Doing Rise {str(RISE)} Run {str(RUN)}")
    run_total=0
    rise_total=0
    hits=0
    misses=0
    for i in range(len(input)):
        
        line=input[i].replace(nl,'')

        if i == 0 or ((i % RISE) != 0):
            #print(f"{line.replace(nl,'')} Skipping line {str(i)}")
            continue  

        run_total += RUN
        index = run_total % len(line)  

        

        hit = (line[index] == "#")
        if hit:
            hits += 1
        #print(f"{line[:index]}{bcolors.OKGREEN}{bcolors.BOLD}{line[index]}{bcolors.ENDC}{line[index+1:]} Should do {str(index)}: Hit {hit} Hits: {str(hits)}")

    print(f"Trees Hit: {bcolors.OKCYAN}{str(hits)}{bcolors.ENDC}")
    return hits

def main():    
    input = get_input("input.txt")

    inputs = [ [input, 1,1], [input, 1,3], [input, 1, 5], [input, 1, 7], [input, 2, 1] ]

    trees_per_slope = list(map(get_trees_for_slope, inputs))

    total = reduce((lambda x,y: x * y), trees_per_slope)
    
    print("Total: {}".format(total)) 

if __name__ == "__main__":
    main()