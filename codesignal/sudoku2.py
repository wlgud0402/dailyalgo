def sudoku(grid):

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # vertical
            vertical = [grid[count][j] for count in range(9)]
            if len(vertical) != len(set(vertical)):
                return False

            # horizontal
            horizontal = grid[i]
            if len(horizontal) != len(set(horizontal)):
                return False

            # box
            if i % 3 == 0 and j % 3 == 0:
                box = [grid[i][j], grid[i][j+1], grid[i][j+2],
                       grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                       grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]]
                if len(box) != len(set(box)):
                    return False

    return True


print(sudoku([[1, 3, 2, 5, 4, 6, 9, 8, 7],
              [4, 6, 5, 8, 7, 9, 3, 2, 1],
              [7, 9, 8, 2, 1, 3, 6, 5, 4],
              [9, 2, 1, 4, 3, 5, 8, 7, 6],
              [3, 5, 4, 7, 6, 8, 2, 1, 9],
              [6, 8, 7, 1, 9, 2, 5, 4, 3],
              [5, 7, 6, 9, 8, 1, 4, 3, 2],
              [2, 4, 3, 6, 5, 7, 1, 9, 8],
              [8, 1, 9, 3, 2, 4, 7, 6, 5]]))  # true
