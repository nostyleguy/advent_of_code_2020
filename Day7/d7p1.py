import sys
import re
from functools import reduce


class Bag():
    def __init__(self, color):
        self.color=color
        self.children=set()

    def add_child(self, bag):
        self.children.append(bag)


def get_input(filename):
    lines =open(filename, "r").readlines()
    bags={}

    for line in lines:
        words = line.split()
        bag = ' '.join(words[0:2])
        words = words[4:]
        children=[]
        if "no other" not in line:
            while len(words) > 0:
                #print(f"Next 4: {str(words[0:4])}")
                children.append((words[0], ' '.join(words[1:3])))
                words=words[4:]     

        bags[bag]=children
    return bags



def search(bags, current, current_children, target):
    if target == current[1]:        
        #print(f" {target} found!")
        return True
    else:
        found = False
        for other in current_children:            
            children_children = bags[other[1]]
            #print(f" Should try: {str(other)}")
            found |= search(bags, other, children_children, target)

        return found

filename = sys.argv[1] if (len(sys.argv) > 1) else "input.txt"
bags=get_input(filename)

def main():
    for item in bags.items():
        print(f"{item[0]} Can contain shiny gold: {str(search(bags, item[0], item[1], 'shiny gold'))}")

    print(f"Total: {str(len([x for x in bags.items() if search(bags, x[0], x[1], 'shiny gold')]))}")

if __name__ == "__main__":
    main()