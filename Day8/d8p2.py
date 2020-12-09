import sys
import copy

def get_input(filename):
    lines =open(filename, "r").readlines()
    #instructions = [tuple(line.split()) for line in lines]
    instructions = {}
    for i in range(len(lines)):
        ls = lines[i].split()
        instructions[i] = [ls[0], int(ls[1].replace('+','')), False]
    return instructions

def run_program(instructions):
    valid = True
    pc=0
    acc=0
    while(True):
        ins = instructions[pc]
        if ins[2] == True:
            print(f"Loop detected at line: {str(pc)}. Aborting. Acc: {str(acc)}")
            valid = False
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
            break
    return (valid, acc)

def main():
    filename = sys.argv[1] if (len(sys.argv) > 1) else "input.txt"
    instructions=get_input(filename)

    for cmd in instructions.items():
        instruction_cpy_modified = copy.deepcopy(instructions)
        if cmd[1][0] == "nop":
            instruction_cpy_modified[cmd[0]][0] = "jmp"
            print(f"Changing {str(cmd[0])} from nop to jmp")
        elif cmd[1][0] == "jmp":                
            instruction_cpy_modified[cmd[0]][0] = "nop"
            print(f"Changing {str(cmd[0])} from jmp to nop")
        else:
            continue
        valid, acc = run_program(instruction_cpy_modified)

        if valid:
            print(f"Got to end of file. Acc: {str(acc)}")
            break
            



if __name__ == "__main__":
    main()