from collections import Counter


def palindromeRearranging(string):
    count = Counter(string).values()
    even = [i for i in count if i % 2 == 0]
    odd = [i for i in count if i % 2 != 0]

    if (len(odd) == 1 or len(odd) == 0) and len(even) + len(odd) == len(Counter(string).keys()):
        return True
    else:
        return False


print(palindromeRearranging("aabb"))

# ''.join(sorted(s, reverse=True))
# print(Counter(string))
# print(Counter(string).items())
# print(Counter(string).keys())
# print(Counter(string).values())
