import sys

def get_input(filename):
    lines =open(filename, "r").readlines()
    instructions = {}
    for i in range(len(lines)):
        ls = lines[i].split()
        instructions[i] = [ls[0], int(ls[1].replace('+','')), False]
    return instructions

def main():
    filename = sys.argv[1] if (len(sys.argv) > 1) else "input.txt"
    instructions=get_input(filename)
    print("\n".join([str(x) for x in instructions.items()]))

    pc=0
    acc=0
    while(True):
        ins = instructions[pc]
        if ins[2] == True:
            print(f"Loop detected at line: {str(pc)}. Aborting. Acc: {str(acc)}")
            break
        else:
            ins[2] = True
            if ins[0] == "nop":
                pc += 1
            elif ins[0] == "acc":
                acc += ins[1]
                pc += 1
            elif ins[0] == "jmp":
                pc += ins[1]
            else:
                print(f"Unrecognized cmd: {ins[0]}.")
        
        if pc == len(instructions):
            print(f"Got to end of file. Acc: {str(acc)}")
            break

if __name__ == "__main__":
    main()