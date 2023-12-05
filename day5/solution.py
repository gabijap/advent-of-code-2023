import collections
import re

seedsToLocation = collections.defaultdict(int)
seedsToSoil = collections.defaultdict(tuple)
soilToFertilizer = collections.defaultdict(tuple)
fertilizerToWater = collections.defaultdict(tuple)
waterToLight = collections.defaultdict(tuple)
lightToTemperature = collections.defaultdict(tuple)
temperatureToHumidity = collections.defaultdict(tuple)
humidityToLocation = collections.defaultdict(tuple)

def storeInfo(input):
    file = open(input, 'r')
    # seeds info
    line = file.readline().strip()
    for num in line.split(' ')[1:]:
        seedsToLocation[int(num)] = 0
    # reading seed-to-soil map:
    line = file.readline()
    line = file.readline()
    line = file.readline()
    while line.strip():
        line = line.strip()
        d, s, c = line.split(' ')
        d, s, c = int(d), int(s), int(c)
        # populateDictionary(d, s, c, seedsToSoil)
        seedsToSoil[s] = (d, c)
        line = file.readline()
    # reading seed-to-soil map:
    line = file.readline()
    line = file.readline()
    while line.strip():
        line = line.strip()
        d, s, c = line.split(' ')
        d, s, c = int(d), int(s), int(c)
        soilToFertilizer[s] = (d, c)
        line = file.readline()
    # reading fertilizer-to-water map:
    line = file.readline()
    line = file.readline()
    while line.strip():
        line = line.strip()
        d, s, c = line.split(' ')
        d, s, c = int(d), int(s), int(c)
        fertilizerToWater[s] = (d, c)
        line = file.readline()
    # reading water-to-light map:
    line = file.readline()
    line = file.readline()
    while line.strip():
        line = line.strip()
        d, s, c = line.split(' ')
        d, s, c = int(d), int(s), int(c)
        waterToLight[s] = (d, c)
        line = file.readline()
    # reading light-to-temperature map:
    line = file.readline()
    line = file.readline()
    while line.strip():
        line = line.strip()
        d, s, c = line.split(' ')
        d, s, c = int(d), int(s), int(c)
        lightToTemperature [s] = (d, c)
        line = file.readline()
    # reading temperature-to-humidity map:
    line = file.readline()
    line = file.readline()
    while line.strip():
        line = line.strip()
        d, s, c = line.split(' ')
        d, s, c = int(d), int(s), int(c)
        temperatureToHumidity[s] = (d, c)
        line = file.readline()
    # reading humidity-to-location map:
    line = file.readline()
    line = file.readline()
    while line.strip():
        line = line.strip()
        d, s, c = line.split(' ')
        d, s, c = int(d), int(s), int(c)
        humidityToLocation[s] = (d, c)
        line = file.readline()

def getLowestLocation():
    for seed in seedsToLocation.keys():
        soil = findNumber(seed, seedsToSoil)
        fertilizer = findNumber(soil, soilToFertilizer)
        water = findNumber(fertilizer, fertilizerToWater)
        light = findNumber(water, waterToLight)
        temperature = findNumber(light, lightToTemperature)
        humidity = findNumber(temperature, temperatureToHumidity) 
        location = findNumber(humidity, humidityToLocation)
        seedsToLocation[seed] = location
    return min(seedsToLocation.values())

def findNumber(source, dictionary):
    for s in dictionary.keys():
        if source >= s and source < (s + dictionary[s][1]):
            return dictionary[s][0] + (source - s)
    return source

if __name__ == "__main__":
    storeInfo('input.txt')
    print(getLowestLocation())