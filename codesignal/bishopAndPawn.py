def bishopAndPawn(bishop, pawn):
    bishop_spot = [ord(bishop[0])-96, int(bishop[1])]
    pawn_spot = [ord(pawn[0])-96, int(pawn[1])]
    return abs(bishop_spot[0] - pawn_spot[0]) == abs(bishop_spot[1] - pawn_spot[1])


print(bishopAndPawn("h1", "h3"))
