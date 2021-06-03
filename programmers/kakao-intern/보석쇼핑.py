def solution(gems):
    kind = {}
    for gem in gems:
        if gem not in kind:
            kind[gem] = 0
        kind[gem] += 1

    start = 0
    end = 0
    for start in range(len(gems)):
        while


print(solution(["DIA", "RUBY", "RUBY", "DIA",
                "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
#[3, 7]
