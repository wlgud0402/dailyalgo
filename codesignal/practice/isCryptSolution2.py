def isCryptSolution(crypt, solution):
    hash_key = {}
    for i in range(len(solution)):
        hash_key[solution[i][0]] = solution[i][1]
    print(hash_key)

    resverse_hash = {}
    for key, value in hash_key.items():
        resverse_hash[value] = key
    print(resverse_hash)

    first = ""
    for s in crypt[0]:
        first += hash_key[s]
    print(first)

    second = ""
    for s in crypt[1]:
        second += hash_key[s]
    print(second)

    if (first[0] == "0" and len(first) > 1) and (second[0] == "0" and len(second) > 1):
        return False

    first_plus_second = str(int(first) + int(second))
    print(first_plus_second)

    answer = ""
    for s in first_plus_second:
        if s in resverse_hash:
            answer += resverse_hash[s]
        else:
            return False

    if answer == crypt[2]:
        return True
    else:
        return False


print(isCryptSolution(["TEN", "TWO", "ONE"], [["O", "1"],
                                              ["T", "0"],
                                              ["W", "9"],
                                              ["E", "5"],
                                              ["N", "4"]]))  # False


print(isCryptSolution(["A",
                       "A",
                       "A"], [["A", "0"]]))  # True
