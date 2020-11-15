def digitDegree(n):
    count = 0
    while len(str(n)) != 1:
        n = sum([int(num) for num in str(n)])
        count += 1

    return count


print(digitDegree(100))  # 1
