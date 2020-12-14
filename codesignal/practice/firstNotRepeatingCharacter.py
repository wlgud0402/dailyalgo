import collections


def firstNotRepeatingCharacter(string):
    count = collections.Counter(string)
    check_one = count.values()
    if 1 not in check_one:
        return "_"
    for s in string:
        if count[s] == 1:
            return s


print(firstNotRepeatingCharacter("abacabad"))  # "c"
