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
                children.append((int(words[0]), ' '.join(words[1:3])))
                words=words[4:]     

        bags[bag]=children
    return bags

def count_bags(bags, current, current_children, total):                
    total += 1
    #print(f"count_bags: {str(current)}, {str(current_children)}, {str(total)}")
    for other in current_children:
        children_children = bags[other[1]]
        for i in range(other[0]):
            total = count_bags(bags, other, children_children, total)

    return total

def main():
    filename = sys.argv[1] if (len(sys.argv) > 1) else "input.txt"
    bags=get_input(filename)
    print(f"Total: {str(count_bags(bags, 'shiny gold', bags['shiny gold'], 0) - 1)}")

if __name__ == "__main__":
    main()