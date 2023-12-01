def getCalibrationValues(input_text):
    """Reads the file line by line and calculates the total calibration values"""

    file = open(input_text, 'r')
    lines = file.readlines()
    count = 0

    for line in lines:
        # read from left
        line_new = line.strip()
        number = ''
        for i in range(len(line_new)):
            if line_new[i].isdigit():
                number += line_new[i]
                break
        # read from right
        for i in range(len(line_new) - 1, -1, -1):
             if line_new[i].isdigit():
                number += line_new[i]
                break  
        count += int(number)     
    return count    

if __name__ == "__main__":
    """Entry point of the script"""
    values = getCalibrationValues("input.txt")
    print(values)