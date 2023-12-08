import re

"""
example input.txt below:

Time:      7  15   30
Distance:  9  40  200
"""

def getProductOfPossibilities(times, distances):
    """Gets the product of possible ways to beat the record for each race"""
    result = 1
    for time, distance in zip(times, distances):
        result *= getCountOfPossibilities(time, distance)

    return result

def getCountOfPossibilities(time, distance):
    """Gets the count of possible ways to beat the record"""
    minTime, maxTime = 0, 0
    for t in range(1, time):
        if (time - t) * t > distance:
            minTime = t
            break
    for t in range(time - 1, 0, -1):
        if (time - t) * t > distance:
            maxTime = t
            break  
    print((maxTime - minTime) + 1)
    return (maxTime - minTime) + 1   

def getData(input):
    """Gets data from the file"""
    file = open(input, 'r')
    line = file.readline()
    time = ''.join([time[0] for time in re.finditer('\d+', line)])
    line = file.readline()
    distance = ''.join([distance[0] for distance in re.finditer('\d+', line)])

    return int(time), int(distance)

if __name__ == "__main__":
    """Entry point of the script"""
    time, distance = getData("input.txt")
    count = getCountOfPossibilities(time, distance)
    print(count)