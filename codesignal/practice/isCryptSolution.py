def isCryptSolution(crypt, solution):
    hash_key = {}
    for i in range(len(solution)):
        hash_key[solution[i][0]] = solution[i][1]
    print(hash_key)

    new_hash = {}
    for key, value in hash_key.items():
        new_hash[value] = key
    print(new_hash)

    first = ""
    second = ""
    for s in crypt[0]:
        first += hash_key[s]

    print("first", first)

    for s in crypt[1]:
        second += hash_key[s]
    print("second", second)

    compare = ""
    new_crypt = str(int(first) + int(second))

    for s in new_crypt:
        compare += new_hash[s]

    return crypt[2] == compare


# print(isCryptSolution(["SEND", "MORE", "MONEY"], [['O', '0'],
#                                                   ['M', '1'],
#                                                   ['Y', '2'],
#                                                   ['E', '5'],
#                                                   ['N', '6'],
#                                                   ['D', '7'],
#                                                   ['R', '8'],
#                                                   ['S', '9']]))  # True


print(isCryptSolution(["TEN", "TWO", "ONE"], [["O", "1"],
                                              ["T", "0"],
                                              ["W", "9"],
                                              ["E", "5"],
                                              ["N", "4"]]))  # False


print(isCryptSolution(["AA",
                       "AA",
                       "BB"], [["A", "1"],
                               ["B", "2"]]))  # True
