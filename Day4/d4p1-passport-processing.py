import re

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
    s=""
    for line in f.readlines():
        if line == nl:
            input.append(s)
            s = ""
        else:
            s += line

    input.append(s)

    return input

FIELDS=['byr','iyr','eyr','hgt','hcl','ecl','pid']


def contains_field(field, PASSPORT):
    return f"{field}:" in PASSPORT

def is_valid(passport):
    #contains_field = list(map((get_trees_for_slope), inputs))

    #total = reduce((lambda x,y: x * y), trees_per_slope)
    results =  [contains_field(f, passport) for f in FIELDS]
    is_valid = (not (False in results))
    print(f"{bcolors.OKCYAN}Passport:{bcolors.ENDC} {passport}Contains Fields: {str(results)} Overall: {is_valid}{nl}{nl}")

    return is_valid


def main():    
    input = get_input("input.txt")
    
    #for passport in input:
    #    print(f"{bcolors.OKCYAN}Passport:{bcolors.ENDC} {passport}Contains Fields: {str(is_valid(passport))}{nl}{nl}")

    valid_passports = [p for p in input if (is_valid(p) == True)]
    invalid_passports = [p for p in input if (is_valid(p) == False)]
    print(f"Valid passports: {str(len(valid_passports))} Invlalid {str(len(invalid_passports))} Total {str(len(input))}")
    
if __name__ == "__main__":
    main()