def solution(boards, skills):
    for skill in skills:
        skill_type, r1, c1, r2, c2, degree = skill
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if skill_type == 1:
                    boards[i][j] -= degree
                else:
                    boards[i][j] += degree

    ok_building_count = 0
    for board in boards:
        cur_ok_building_count = len([b for b in board if b > 0])
        ok_building_count += cur_ok_building_count
    return ok_building_count


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [
      [1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
