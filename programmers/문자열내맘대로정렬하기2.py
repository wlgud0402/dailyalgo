def solution(strings, n):
    strings.sort()

    strings = [list(s) for s in strings]
    sorted_strings = sorted(strings, key=lambda x: x[n])

    sorted_strings = ["".join(s) for s in sorted_strings]

    return sorted_strings


print(solution(["abce", "abcd", "cdx"]	, 2))  # [car, bed, sun]
print(solution(["sun", "bed", "car"]	, 1))  # [abcd, abce, cdx]
