MAP = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}

def preProcess(line):
    "Preprocesses the string by replacing digit words to the corresponding replacement value"

    for number in MAP.keys():
        line = line.replace(number, MAP[number])
    return line

def getCalibrationValue(line):
    "Calculates calibration values for the string"

    line = preProcess(line)
    number = ''
    count = 0
    # read from left
    for i in range(len(line)):
        if line[i].isdigit():
            number += line[i]
            break
    # read from right
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            number += line[i]
            break  
    count += int(number)   
    
    return count

def getCalibrationValues(input):
    "Reades the input file line by line and calculates the total calibration value"

    file = open(input, 'r')
    lines = file.readlines()
    count = 0  

    for line in lines:
        count += getCalibrationValue(line.strip())
    return count

if __name__ == "__main__":
    """Entry point of the script"""
    values = getCalibrationValues("input2.txt")
    print(values)