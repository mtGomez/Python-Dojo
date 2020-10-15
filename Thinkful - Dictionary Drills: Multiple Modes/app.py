from collections import Counter


def modes(data):
    myMap = Counter(data)
    maximum = max(myMap.values())
    sortedMap = sorted([key for key,value in myMap.items() if value == maximum])
    return [] if len(myMap) == len(sortedMap) else sortedMap
