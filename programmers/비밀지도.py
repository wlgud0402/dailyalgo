def solution(n, arr1, arr2):
    bin_arr1 = []
    bin_arr2 = []

    for line in arr1:
        bin_line = bin(line)
        if len(bin_line) == n + 2:
            bin_line = bin_line[2:]
            bin_arr1.append(list(bin_line))
        else:
            bin_line = ("0" * n) + bin_line[2:]
            bin_line = bin_line[-n:]
            bin_arr1.append(list(bin_line))

    for line in arr2:
        bin_line = bin(line)
        if len(bin_line) == n + 2:
            bin_line = bin_line[2:]
            bin_arr2.append(list(bin_line))
        else:
            bin_line = ("0" * n) + bin_line[2:]
            bin_line = bin_line[-n:]
            bin_arr2.append(list(bin_line))

    new_map = []
    for i in range(len(bin_arr1)):
        one_line = []
        for j in range(len(bin_arr1)):
            if bin_arr1[i][j] == "0" and bin_arr2[i][j] == "0":
                one_line.append(" ")
            else:
                one_line.append("#")
        new_map.append(one_line)

    for i in range(len(new_map)):
        new_map[i] = ''.join(new_map[i])
    return new_map


# # ["#####","# # #", "### #", "# ##", "#####"]
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))

# new = bin(20)
# newnew = new + "1"
# print(int(newnew, 2))
