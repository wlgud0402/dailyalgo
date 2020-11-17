import copy


def buildPalindrome(s):
    insert_idx = 1
    first_s = copy.deepcopy(s)
    while s != s[::-1]:
        insert_s = s[:insert_idx]
        s = first_s + insert_s[::-1]
        insert_idx += 1

    return s


print(buildPalindrome("abcabc"))  # abcab c bacba
