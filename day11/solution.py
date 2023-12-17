
"""
example input.txt below:

...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

def getImage(input):
    """Reads image from the input file"""

    file = open(input, "r")
    image = file.read().strip().split("\n")
    return image

def getCoordinates(image):
    """Gets coordinates of galaxies denoted as #"""

    coordinates = []
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == "#":
                coordinates.append((i, j))
    return coordinates

def getDistance(p1, p2, empty_rows, empty_cols):
    """
    Gets distance between two points. If it's an empty row or column, 
    adds extra steps to the distance.
    """

    i1, j1 = p1
    i2, j2 = p2
    
    i1, i2 = min(i1, i2), max(i1, i2)
    j1, j2 = min(j1, j2), max(j1, j2)

    distance = 0
    for i in range(i1, i2):
        distance += 1
        if empty_rows[i]:
            distance += 10**6 - 1
    for j in range(j1, j2):
        distance += 1
        if empty_cols[j]:
            distance += 10**6 - 1
    return distance   

def getSumOfDistances(image):
    """Gets sum of distances between all pairs of points"""

    empty_rows = [all([image[i][j] == '.' for j in range(len(image[0]))]) for i in range(len(image))]
    empty_cols = [all([image[i][j] == '.' for i in range(len(image))]) for j in range(len(image[0]))]

    coordinates = getCoordinates(image)
    sum_distances = 0
    for idx1 in range(len(coordinates)):
        for idx2 in range(idx1+1, len(coordinates)):
            sum_distances += getDistance(coordinates[idx1], coordinates[idx2], empty_rows, empty_cols)
    return sum_distances

if __name__ == "__main__":
    """Entry point of the script"""

    image = getImage('input.txt')
    print(getSumOfDistances(image))
