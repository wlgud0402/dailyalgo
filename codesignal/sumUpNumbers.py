def sumUpNumbers(inputString):
    numbers = []
    number = ""
    for i in range(len(inputString)):
        if inputString[i].isdigit():
            number += inputString[i]
        else:
            if number != "":
                numbers.append(number)
                number = ""

    if number != "":
        numbers.append(number)

    numbers = sum([int(i) for i in numbers])
    return numbers


print(sumUpNumbers("42+781"))  # 823
