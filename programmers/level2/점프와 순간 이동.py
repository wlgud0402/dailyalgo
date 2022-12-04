from collections import deque


def solution(n):
    queue = deque()
    visited = set()

    queue.append((0, 0, 0))
    visited.add((0, 0, 0))
    answers = set()
    while queue:
        cur_position, cur_move_distance, total_used = queue.popleft()

        if cur_position == n:
            answers.add(total_used)
            continue

        jump = (cur_position + 1, cur_move_distance + 1, total_used + 1)
        teleport = (cur_move_distance * 2, cur_move_distance * 2, total_used)
        if jump not in visited and jump[0] <= n:
            visited.add(jump)
            queue.append(jump)

        if teleport not in visited and teleport[0] <= n:
            visited.add(teleport)
            queue.append(teleport)

    answers = list(answers)
    return sorted(answers)[0]


print(solution(5000))
