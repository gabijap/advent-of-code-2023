"""
example input.txt below:

0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""
def getTotal(data):
    """Gets total of next numbers"""
    total = 0
    for numbers in data:
        total += getNextNumber(numbers)
    return total

def getNextNumber(numbers):
    """Gets the next number after extrapolating the numbers"""
    rows = [numbers]
    while not all(num == 0 for num in rows[-1]):
        rows.append([rows[-1][i] - rows[-1][i-1] for i in range(len(rows[-1]) - 1, 0, -1)][::-1])
    total = 0
    for i in range(len(rows) - 1, -1, -1):
        total = (rows[i][0] - total)
    return total

def getData(input):
    """Gets data from the file"""
    file = open(input, "r")
    lines = file.readlines()
    numbers = [[int(num) for num in line.strip().split(' ')] for line in lines]
    return numbers

if __name__ == "__main__":
    """Entry point of the script"""
    data = getData("input.txt")
    total = getTotal(data)
    print(total)