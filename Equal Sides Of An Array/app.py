def find_even_index(arr):
    for index in range(len(arr)):
        leftSide = sum(arr[:index])
        rightSide = sum(arr[index+1:])
        if (leftSide == rightSide):
            return index
    return -1
