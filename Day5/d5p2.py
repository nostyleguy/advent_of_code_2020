import re
import sys
import functools

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

def boardingpass_comparator(first, second):
    first_row = first[:7]
    first_col = first[7:]
    second_row = second[:7]
    second_col = second[7:]

    if first_row == second_row:
        if first_col == second_col:
            return 0
        else:
            return 1 if second_col < first_col else -1
    else:
        return 1 if first_row < second_row else -1


def do_it(x):
    return 8 * divide(x[:7],0,127)  + divide(x[7:], 0, 7)


def main():  
    filename = sys.argv[1] if (len(sys.argv) > 1) else "input.txt"
    input=get_input(filename)
    input.remove('')

    input.sort(key=functools.cmp_to_key(boardingpass_comparator))

    seat_numbers=list(map(do_it, input))

    for i in range(1, len(input) - 1):  
        prev=seat_numbers[i-1]
        next=seat_numbers[i+1]

        print(f"{str(i)} {input[i]} Prev: {str(prev)} This: {str(seat_numbers[i])} Next: {str(next)} Diff: {str(next-prev)}")
        if ((next - prev) != 2):
            print(f" **** {str(i)} {input[i]} Prev: {str(prev)} This: {str(seat_numbers[i])} Next: {str(next)} Diff: {str(next-prev)}") 
            break

    

    #print(f"{str(input)}")
    #print(f"Max: {str(max(map(lambda x : (8 * divide(x[:7],0,127)  + divide(x[7:], 0, 7)) , input)))}")

    
if __name__ == "__main__":
    main()