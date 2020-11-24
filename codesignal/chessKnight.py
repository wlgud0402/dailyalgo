# use ord
# max 8
def chessKnight(cell):
    x = ord(cell[0])-96
    y = int(cell[1])

    LLU = (x-2, y+1)
    LLD = (x-2, y-1)
    RRU = (x+2, y+1)
    RRD = (x+2, y-1)
    UUR = (x+1, y+2)
    UUL = (x-1, y+2)
    DDR = (x+1, y-2)
    DDL = (x-1, y-2)

    position = [LLU, LLD, RRU, RRD, UUR, UUL, DDR, DDL]
    count = 0
    for i in range(len(position)):
        if 0 < position[i][0] < 9 and 0 < position[i][1] < 9:
            count += 1
    return count


print(chessKnight("a1"))  # 2
print(chessKnight("c2"))  # 6
# chess board 8x8
