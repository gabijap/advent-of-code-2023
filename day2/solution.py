import re

CONFIGURATION = {"red": 12, "green": 13, "blue": 14}

def isPossible(line):
    """Checks if the game is possible based on the cube configurations
       Performs cheks on each sub-game
    """

    for subGame in line.split(";"):
        cubes = re.findall(r"\d+ blue|\d+ red|\d+ green", subGame)
        counts = {"red": 0, "green": 0, "blue": 0}
        for cube in cubes:
            cube = cube.split(" ")
            counts[cube[1]] += int(cube[0])
            if counts[cube[1]] > CONFIGURATION[cube[1]]:
                return False
    return True

def getPossibleGames(input):
    """Gets a set of all possible games"""

    lines = getLines(input)
    count = 0
    result = set()

    for line in lines:
        line = line.strip()
        if isPossible(line):
            game = int(re.search(r'\d+', line)[0])
            result.add(game)
    return result

def getPowerOfCubes(line):
    """Gets a power of minimum cubes required for the game"""
    
    maxRed, maxGreen, maxBlue = 0, 0, 0

    for subGame in line.split(";"):
        cubes = re.findall(r"\d+ blue|\d+ red|\d+ green", subGame)
        counts = {"red": 0, "green": 0, "blue": 0}
        for cube in cubes:
            cube = cube.split(" ")
            counts[cube[1]] += int(cube[0])
        maxRed = max(maxRed, counts["red"])
        maxGreen = max(maxGreen, counts["green"])
        maxBlue = max(maxBlue, counts["blue"])
    
    return maxRed * maxGreen * maxBlue

def getPowers(input):
    """Gets a list of powers of minimum cubes required for each game"""

    lines = getLines(input)
    count = 0
    result = []

    for line in lines:
        line = line.strip()
        result.append(getPowerOfCubes(line))
    return result

def getLines(input):
    """Reads lines from the file"""

    file = open(input, 'r')
    lines = file.readlines()
    return lines

if __name__ == "__main__":
    """Entry point of the script"""

    result1 = getPossibleGames("input.txt")
    result2 = getPowers("input.txt")