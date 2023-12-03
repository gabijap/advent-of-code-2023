import collections
import re

def getNumbersRatio(input):
    """
    Finds all * symbols that are adjacent to exactly two numbers
    and calculates ratios (product of two numbers) for each finding
    """

    lines = getLines(input)
    lines = [line.strip() for line in lines]
    numbers = []
    dictionary = collections.defaultdict(set)

    for i, line in enumerate(lines):
        for match in re.finditer(r'\d+', line):
            for j in range(match.span()[0], match.span()[1]):
                # check left
                if check(lines, i, j - 1):
                    dictionary[(i, j - 1)].add((i, match.span()[0], match.span()[1]))
                # check right
                if check(lines, i, j + 1):
                    dictionary[(i, j + 1)].add((i, match.span()[0], match.span()[1]))
                    break
                # check top
                if check(lines, i - 1, j):
                    dictionary[(i - 1, j)].add((i, match.span()[0], match.span()[1]))
                # check bottom
                if check(lines, i + 1, j):
                    dictionary[(i + 1, j)].add((i, match.span()[0], match.span()[1]))
                # check top left
                if check(lines, i - 1, j - 1):
                    dictionary[(i - 1, j - 1)].add((i, match.span()[0], match.span()[1]))
                # check top right
                if check(lines, i - 1, j + 1):
                    dictionary[(i - 1, j + 1)].add((i, match.span()[0], match.span()[1]))
                # check botom left
                if check(lines, i + 1, j - 1):
                    dictionary[(i + 1, j - 1)].add((i, match.span()[0], match.span()[1])) 
                # check botom right
                if check(lines, i + 1, j + 1):
                    dictionary[(i + 1, j + 1)].add((i, match.span()[0], match.span()[1]))

    for element in dictionary.keys():
        if len(dictionary[element]) == 2:
            num1 = lines[list(dictionary[element])[0][0]][list(dictionary[element])[0][1]:list(dictionary[element])[0][2]]
            num2 = lines[list(dictionary[element])[1][0]][list(dictionary[element])[1][1]:list(dictionary[element])[1][2]]
            numbers.append(int(num1) * int(num2))

    return numbers

def check(lines, i, j):
    """Checks if a current char is *"""
    
    if i < 0 or j < 0 or i >= len(lines) or j >= len(lines[0]):
        return False
    return lines[i][j] == '*'

def getLines(input):
    """Reads lines from the file"""

    file = open(input, 'r')
    lines = file.readlines()
    return lines

if __name__ == "__main__":
    """Entry point of the script"""

    ratios = getNumbersRatio("input.txt")
    print(ratios)
    print(sum(ratios))