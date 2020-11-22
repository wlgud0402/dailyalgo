def isMAC48Address(inputString):
    finding = ["A", "B", "C", "D", "E", "F", "0",
               "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    address = inputString.split('-')
    for i in range(len(address)):
        if len(address[i]) != 2:
            return False
        for j in range(2):
            if address[i][j] in finding:
                continue
            else:
                return False

    return True


print(isMAC48Address("00-1B-63-84-45-E6"))  # true
