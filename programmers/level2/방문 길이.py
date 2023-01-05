def solution(directions):

    # 이동하는 경로의 중복 제거를 위해 set을 사용합니다.
    paths = set()

    # 현재위치를 [0,0]으로 초기화 합니다.
    position = [0, 0]

    # 이동후의 위치 갱신을 위해 방향에 따른 x, y값 위치 변경 값을 map에 설정합니다.
    move_map = {
        "L": [0, -1],
        "U": [-1, 0],
        "R": [0, 1],
        "D": [1, 0]
    }

    for direction in directions:
        before = position[:]
        new_position = [position[0] + move_map[direction]
                        [0], position[1] + move_map[direction][1]]
        # 이동한 위치가 맵에서 벗어나지 않아야 하기 때문에 -5 ,5 를 기준으로 값을 확인합니다.
        if -5 <= new_position[0] <= 5 and -5 <= new_position[1] <= 5:
            position = new_position
            # 경로의 경우 시작위치와 이동 후 위치를 정렬한 값을 경로로 설정합니다 -> 중복제거를 위함
            path_set = sorted([before, position])
            path = ((path_set[0][0], path_set[0][1]),
                    (path_set[1][0], path_set[1][1]))
            paths.add(path)
    return len(paths)
