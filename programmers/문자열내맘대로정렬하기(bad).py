from functools import cmp_to_key

a = [1,65,4,3,6,7,34,4]

print("abc" > "abd")

def compare(a, b):
    if a[1] > b[1]:
        return -1
    elif a[1] == b[1]:
        if a>b:
            return -1
        else:
            return 1
    else:
        return 1


print(sorted(a, key=cmp_to_key(compare)))