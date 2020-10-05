def solution(brown, yellow):
    all_blocks = brown + yellow

    # for i in range(3, all_blocks+1): 3보다 작은경우는 볼 필요가 없다.
    for i in range(1, all_blocks+1):
        if all_blocks % i == 0:
            height = i
            width = all_blocks // height

            if (width-2) * (height-2) == yellow:
                return [width, height]

    # possibles = []
    # all_blocks = brown + yellow
    # for i in range(1, all_blocks+1):
    #     for j in range(1, all_blocks+1):
    #         pair = [i, j]
    #         pair.sort(reverse=True)

    #         if pair not in possibles and i * j == all_blocks:
    #             possibles.append(pair)

    # for possible in possibles:
    #     width = possible[0] - 2
    #     heigth = possible[1] - 2

    #     if width * heigth == yellow:
    #         return [possible[0], possible[1]]


print(solution(24, 24))
# return 4,3
# 노랑색의 가로 = 갈색의 가로 -2
# 노랑색의 세로 = 갈색의 ㅅ로 -2
