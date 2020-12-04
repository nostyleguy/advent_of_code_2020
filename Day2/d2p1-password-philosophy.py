import sys
import re

nl = '\n'

def get_input(filename):
    f = open(filename, "r")
    input = []
    for line in f.readlines():
        input.append(line)
    return input

def process_line(lower, upper, letter, password):
    c = password.count(letter)
    return c >= int(lower) and c <= int(upper)

def main():
    valid_c = 0
    input = get_input("input.txt")
    for line in input:        
        regex = re.compile(r"([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)\n", )
        match = re.search(regex, line)
        if match:
            lower=match.group(1)
            upper=match.group(2)
            letter=match.group(3)
            password=match.group(4)
            
            valid = process_line(lower,upper,letter,password)

            if valid:
                valid_c += 1
            print(f"Line: {line.replace(nl,'')} = Lower: {lower} Upper: {upper} Letter: {letter} Password: {password} Valid: {valid}")
        else:
            print(f"{line} Doesn't match regex :(")

    print(f"Valid: {str(valid_c)}")

if __name__ == "__main__":
    main()