from collections import Counter

def find_it(seq):
    mappedValues = Counter(seq)
    for key, value in mappedValues.items():
        if(value % 2 != 0):
            return key
    return -1
