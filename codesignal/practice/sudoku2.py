def sudoku2(grid):

    for i in range(len(grid)):
        horizontal = [grid[i][count]
                      for count in range(9) if grid[i][count] != '.']
        print("horizantal: ", horizontal)
        if len(horizontal) != len(set(horizontal)):
            return False

        vertical = [grid[count][i]
                    for count in range(9) if grid[count][i] != '.']
        if len(vertical) != len(set(vertical)):
            return False

        for j in range(len(grid[0])):

            # box
            if i % 3 == 0 and j % 3 == 0:
                box = [grid[i][j], grid[i][j+1], grid[i][j+2],
                       grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                       grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]]
                box = [box[i] for i in range(len(box)) if box[i] != '.']
                if len(box) != len(set(box)):
                    return False

    return True


print(sudoku2([[".", ".", "4", ".", ".", ".", "6", "3", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", "."],
               ["5", ".", ".", ".", ".", ".", ".", "9", "."],
               [".", ".", ".", "5", "6", ".", ".", ".", "."],
               ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
               [".", ".", ".", "7", ".", ".", ".", ".", "."],
               [".", ".", ".", "5", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", "."]]))  # false
