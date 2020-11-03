def chessBoardCellColor(cell1, cell2):
    cell1_color = ""
    cell2_color = ""
    if ord(cell1[0]) % 2 == 0:
        if int(cell1[1]) % 2 == 0:
            cell1_color = "Brown"
        else:
            cell1_color = "Orange"

    else:
        if int(cell1[1]) % 2 == 0:
            cell1_color = "Orange"
        else:
            cell1_color = "Brown"

    if ord(cell2[0]) % 2 == 0:
        if int(cell2[1]) % 2 == 0:
            cell2_color = "Brown"
        else:
            cell2_color = "Orange"

    else:
        if int(cell2[1]) % 2 == 0:
            cell2_color = "Orange"
        else:
            cell2_color = "Brown"

    return cell1_color == cell2_color


print(chessBoardCellColor("A1", "B2"))
