import re


def divideAndConquer(n1, operator, n2, n3, lowerLimit, setOfNumbers):
    for n in range(lowerLimit, 10):
        if(str(n) not in setOfNumbers):
            number1 = int(n1.replace("?", str(n)))
            number2 = int(n2.replace("?", str(n)))
            number3 = int(n3.replace("?", str(n)))

            if operator == "+":
                number1 = number1+number2
            if operator == "-":
                number1 = number1-number2
            if operator == "*":
                number1 = number1*number2

            if(number1 == number3):
                return n
    return -1


def solve_runes(runes):
    search = re.search(number+op+number+asig+number, runes)
    n1 = search.group(1)
    operator = search.group(2)
    n2 = search.group(3)
    n3 = search.group(4)
    setOfNumbers = set((n1+n2+n3).replace("?", "").replace("-", ""))

    if(n1.startswith("-?") or n2.startswith("-?") or n3.startswith("-?") or (n1.startswith("?") and len(n1) > 1) or (n2.startswith("?") and len(n2) > 1) or (n3.startswith("?") and len(n3) > 1)):
        result = divideAndConquer(n1, operator, n2, n3, 1, setOfNumbers)
    else:
        result = divideAndConquer(n1, operator, n2, n3, 0, setOfNumbers)
    return result


number = r"(0|\-?[1-9?][0-9?]*)"
op = r"(\+|\-|\*)"
asig = r"\="
