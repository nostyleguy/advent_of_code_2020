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
    input = []
    s=""
    for line in f.readlines():
        if line == nl:
            input.append(s)
            s = ""
        else:
            s += line.replace(nl,' ')

    input.append(s)

    return input


def validate_height(s):
    v=int(s[:-2])
    if "in" in s:
        return v in range(59,77)
    else:
        return v in range(150,194)

FIELDS=[
    ('byr','^\d{4}$', (lambda x: (int(x) in range(1920,2003)))),
    ('iyr','^\d{4}$', (lambda x: (int(x) in range(2010,2021)))),
    ('eyr','^\d{4}$', (lambda x: (int(x) in range(2020,2031)))),
    ('hgt','^\d+(cm|in)$', validate_height),
    ('hcl','^#[0-9a-f]{6}$', (lambda x: True)),
    ('ecl','\S*', (lambda x: x in ['amb','blu','brn','gry','grn','hzl','oth'] )),
    ('pid','^\d{9}$',(lambda x: True )),
]


def valid_field(field, passport):
    regex = re.compile(rf"{field[0]}:(\S*)",)
    field_match = re.search(regex, passport)
    if field_match:
        print(f'  Contains Field: {bcolors.OKCYAN}{field[0]}{bcolors.ENDC} : {field_match.group(1)}')
        regex=re.compile(rf'{field[1]}')
        value_match=re.match(regex,field_match.group(1))
        if value_match:
            print(f'   {bcolors.OKGREEN}Value syntax is valid for {field[1]}:{bcolors.ENDC} {field_match.group(1)}: {value_match.group(0)}')            
            if field[2](value_match.group(0)):
                print(f"    {bcolors.OKGREEN}Value semantics are valid!{bcolors.ENDC}")
                return True
            else:
                print(f"    {bcolors.FAIL}Value semantics are valid!{bcolors.ENDC}")
                return False
        else:
            print(f"   {bcolors.FAIL}Value syntax is invalid: {bcolors.ENDC}{field_match.group(1)}")
            return False
    else:
        print(f"  Doesn't contain field: {bcolors.FAIL}{field[0]}{bcolors.ENDC}")
        return False


def is_valid(passport):
    print(f"{bcolors.OKCYAN}Passport:{bcolors.ENDC} {passport}")
    results =  [valid_field(f, passport) for f in FIELDS]
    is_valid = (not (False in results))
    print(f"Valid Fields: {str(results)} Overall: {is_valid}{nl}{nl}")

    return is_valid


def main():  
    filename = sys.argv[1] if (len(sys.argv) > 1) else "input.txt"
    passports = get_input(filename)
    valid_passports = [p for p in passports if is_valid(p) ]
    print(f"Valid passports: {str(len(valid_passports))}")
    
if __name__ == "__main__":
    main()