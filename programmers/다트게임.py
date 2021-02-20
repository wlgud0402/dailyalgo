def solution(dartResult):
    answer = 0
    cal = {
        "S": 1,
        "D": 2,
        "T": 3,
    }
    option = {
        "*": 2,
        "#": -1,
    }

    numbers = [1, 1, 1]
    num_idx = 0
    for i in range(len(dartResult)):
        try:
            num = int(dartResult[i])
            pass
        except:
            pass


print(solution("1S2D*3T"))  # 37
