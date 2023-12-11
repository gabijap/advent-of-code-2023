import collections
import re
from math import gcd
from functools import reduce

"""
example input.txt below:

RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

def lcm(numbers):
    """Function for finding least common multiplier"""
    return reduce(lambda a,b: a*b // gcd(a,b), numbers)

def isNodeEndingWith(node, letter):
    """Checks if node is ending with a specified letter"""
    return node[-1] == letter

def getCountOfMoveForNode(instruction, mapping, node):
    """Gets count of moves required to reach a node ending with Z from a node ending with A"""
    moves = 0
    i = 0
    while not isNodeEndingWith(node, 'Z'):
        if instruction[i] == 'L':
            node = mapping[node][0]
        else:
            node = mapping[node][1]
        moves += 1
        i += 1
        if i >= len(instruction):
            i = 0

    return moves

def getCountOfMoves(instruction, mapping):
    """Gets count of moves required reaching all nodes ending with Z from all nodes ending with A"""
    sources = [node for node in mapping.keys() if isNodeEndingWith(node, 'A')]
    moves = [getCountOfMoveForNode(instruction, mapping, source) for source in sources]

    return lcm(moves)

def getData(input):
    """Gets data from the file"""
    file = open(input, 'r')
    instruction = ''
    dictionary = collections.OrderedDict()
    line = file.readline()
    while line.strip():
        instruction += line.strip()
        line = file.readline()

    line = file.readline()
    while line.strip():
        data = re.findall('[0-9A-Za-z]+', line)
        dictionary[data[0]] = (data[1], data[2])
        line = file.readline()

    return instruction, dictionary
    
if __name__ == "__main__":
    """Entry point of the script"""
    instruction, dictionary = getData('input.txt')
    moves = getCountOfMoves(instruction, dictionary)
    print(moves)