import collections


def fileNaming(names):
    hash_map = collections.Counter(names)
    print(hash_map)


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
