import collections
from functools import cmp_to_key
import re

"""
example input.txt below:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

def getTotalWinnings(data):
    """Get the total of winnings"""
    total = 0
    rank = len(data)
    dictionary = createSortedHandsDictionary(data)
    for hands in dictionary.keys():
        for hand in dictionary[hands]:
            total += (rank * hand[1])
            rank -= 1
    return total

def compare(hand1, hand2):
    """Custom comparison function"""
    strength = {
        'A': 13,
        'K': 12,
        'Q': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
        'J': 1
    }
    for c1, c2 in zip(hand1[0], hand2[0]):
        if c1 != c2 and strength[c1] > strength[c2]:
            return -1
        elif c1 != c2 and strength[c1] < strength[c2]:
            return 1
    return 1

def createSortedHandsDictionary(data):
    """Populates hands dictionary based on the given data"""
    handsDictioanry = collections.OrderedDict()
    handsDictioanry['Five of a kind'] = []
    handsDictioanry['Four of a kind'] = []
    handsDictioanry['Full house'] = []
    handsDictioanry['Three of a kind'] = []
    handsDictioanry['Two pair'] = []
    handsDictioanry['One pair'] = []
    handsDictioanry['High card'] = []

    for hand, bid in data.items():
       handsDictioanry[getHandsType(hand)].append((hand, bid))
    for hand in handsDictioanry.keys():
        handsDictioanry[hand] = sorted(handsDictioanry[hand], key=cmp_to_key(compare))

    return  handsDictioanry

def getHandsType(hand):
    """Given a hand, determines its type"""
    counter = collections.Counter([c for c in hand])
    product = 1
    for count in counter.values():
        product *= count
    if len(counter) == 1 or (len(counter) == 2 and 'J' in counter):
        return 'Five of a kind'
    if len(counter) == 2 and 'J' not in counter:
        if list(counter.values())[0] == 1 or list(counter.values())[0] == 4:
            return 'Four of a kind'
        return 'Full house'
    if len(counter) == 3 and 'J' in counter:
        if counter['J'] == 3:
            return 'Four of a kind'
        if counter['J'] == 2 and product == 4:
            return 'Four of a kind'
        if counter['J'] == 2 and product == 2:
            return 'Three of a kind'
        if counter['J'] == 1 and product == 2:
            return 'Four of a kind'
        if counter['J'] == 1 and product == 4:
            return 'Full house'
        if counter['J'] == 1 and product == 3:
            return 'Four of a kind'
    if len(counter) == 3:
        product = 1
        for count in counter.values():
            product *= count
        if product == 3:
            return 'Three of a kind'
        return 'Two pair'
    if len(counter) == 4 and 'J' in counter:
        return 'Three of a kind'
    if len(counter) == 4 or (len(counter) == 5 and counter['J'] == 1):
        return 'One pair'
    return 'High card'

def getData(input):
    """Gets data from the input file"""
    file = open(input, 'r')
    lines = file.readlines()
    data = dict([(line.split(' ')[0], int(line.split(' ')[1])) for line in lines])
    return data

if __name__ == "__main__":
    data = getData('input.txt')
    total = getTotalWinnings(data)
    print(total)