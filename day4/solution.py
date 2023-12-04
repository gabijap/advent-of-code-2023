import collections
import re

def getCountOfScratchcards(input):
    """Gets the number of scratch cards"""

    lines = [line.strip() for line in getLines(input)]
    counter = collections.defaultdict(int)
    
    for i, line in enumerate(lines):
        first_part, second_part = line.split('|') 
        first_part = first_part.split(':')[-1]
        first_part = first_part.strip()
        second_part = second_part.strip()
        winning_numbers = set(re.findall('\d+', first_part))
        numbers_have = set(re.findall('\d+', second_part))
        qualified_numbers = winning_numbers.intersection(numbers_have)
        print(i + 1, len(qualified_numbers))
        if len(qualified_numbers) > 0:
            # populate the counter
            for j in range(1, len(qualified_numbers) + 1):
                counter[(i+1) + j] += (1 + counter[(i+1)])
        counter[(i+1)] += 1

    return sum(counter.values())

def getLines(input):
    """Reads lines from the file"""

    file = open(input, 'r')
    lines = file.readlines()
    return lines

if __name__ == "__main__":
    """Entry point of the script"""
    count = getCountOfScratchcards("input.txt")
    print(count)