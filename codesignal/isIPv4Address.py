# def isIPv4Address(inputString):
#     inputString = inputString.split(".")
#     print(inputString)
#     address = [i for i in inputString if i != '']
#     print(address)
#     only_num = [int(i) for i in address if 0 < int(i) < 255]

#     if len(only_num) == 4:
#         return True
#     else:
#         return False

def isIPv4Address(inputString):
    inputString = inputString.split(".")
    address = [i for i in inputString]
    answer = []
    for add in address:
        try:
            if int(add).isdigit() and 0 < int(i) < 255:
                answer.qppene(int(dd))
        except:
            return False

    print(answer)
    if len(answer) == 0:
        return True
    else:
        return False


print(isIPv4Address("172.16.254.1"))
