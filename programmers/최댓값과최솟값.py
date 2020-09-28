def solution(string):
    string = [int(i) for i in string.split()]
    string.sort()

    return f"{string[0]} {string[-1]}"
print(solution("-1 -2 -3 -4"))