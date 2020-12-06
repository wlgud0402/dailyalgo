import collections


def fileNaming(names):
    hash_map = collections.Counter(names)
    print(hash_map)
    answer = []
    for i in range(1, len(hash_map)):
        compare = names[:i]
        if names[i] in compare and hash_map[names[i]]:
            hash_map[names[i]] -= 1


print(fileNaming([
    "name",
    "name",
    "name(1)",
    "name(3)",
    "name(2)",
    "name(2)"]))

# ["name",
#  "name(1)",
#  "name(1)(1)",
#  "name(3)",
#  "name(2)",
#  "name(2)(1)"]
