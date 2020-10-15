def successor(index, args):
    subIndex = index
    while subIndex+1 < len(args) and args[subIndex+1]-1 == args[subIndex]:
        subIndex = subIndex + 1
    if(subIndex-index < 2):
        return None, index
    return args[subIndex], subIndex


def solution(args):
    index = 0
    res = ""
    while index < len(args):
        bound, currentIndex = successor(index, args)
        if(bound == None):
            res = res+(str(args[index])+",")
        else:
            res = res+(str(args[index])+"-"+str(args[currentIndex])+",")
        index = currentIndex + 1
    return res[:-1]
