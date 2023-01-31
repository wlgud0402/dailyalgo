def solution(m, n, board):
    board = [list(i) for i in board]
    removed_block_count = 0
    destroyed_blocks = []
    while True:
        # 4개가 서로 같고 "0" 이 아닌지 확인해서 4개의 점을 추가해줌
        for row in range(m-1):
            for col in range(n-1):
                if board[row][col] == board[row][col+1] == board[row+1][col] == board[row+1][col+1] and board[row][col] != "0":
                    destroyed_blocks.append((row, col))
                    destroyed_blocks.append((row, col+1))
                    destroyed_blocks.append((row+1, col))
                    destroyed_blocks.append((row+1, col+1))

        # 4개가 같아서 지워야 하는 블럭이 없으면 break
        if len(destroyed_blocks) == 0:
            break

        # 확인 지점이 "0" 이아니라면 removed_block_count += 1
        for destroyed_block in destroyed_blocks:
            r, c = destroyed_block
            if board[r][c] != "0":
                board[r][c] = "0"
                removed_block_count += 1

        # 삭제하는 블록 리스트 초기화
        destroyed_blocks = []

        # 위의 지점을 아래로 땡겨주기
        is_moved = True
        while is_moved:
            is_moved = False
            for row in range(1, m):
                for col in range(n):
                    if board[row][col] == "0" and board[row-1][col] != "0":
                        is_moved = True
                        board[row][col] = board[row-1][col]
                        board[row-1][col] = "0"

    return removed_block_count


print(solution(	6, 6, ["TTTANT", "RRFACC",
                       "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
