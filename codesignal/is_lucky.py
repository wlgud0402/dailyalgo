def isLucky(n):
    mid = len(str(n)) // 2
    front = [int(i) for i in str(n)[:mid]]
    end = [int(i) for i in str(n)[mid:]]
    return sum(front) == sum(end)

print(isLucky(134008))


