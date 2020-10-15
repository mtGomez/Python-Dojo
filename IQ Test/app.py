def iq_test(numbers):
    listOfNumbers = [int(n) for n in numbers.split(" ")]
    listOfEvenNumbers = [n for n in listOfNumbers if (n % 2 == 0)]
    listOfOddNumbers = [n for n in listOfNumbers if (n % 2 != 0)]
    if(len(listOfEvenNumbers) == 1):
        return listOfNumbers.index(listOfEvenNumbers[0])+1
    else:
        return listOfNumbers.index(listOfOddNumbers[0])+1
    return -1
