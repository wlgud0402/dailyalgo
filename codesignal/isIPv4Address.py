def isIPv4Address(inputString):
    inputString = inputString.split(".")
    answer = []
    for address in inputString:
        if address.isdigit() and len(address) == len(str(int(address))) and 0 <= int(address) <= 255:
            answer.append(address)
        else:
            return False

    if len(answer) == 4:
        return True
    else:
        return False


print(isIPv4Address("01.254.255.0"))
