# -*- coding: utf-8 -*-
#rjust , zfill
# rjust는 원하는 만큼의 값을 채워줌 <<앞에>> rjust(width, [fillchar])
# ljust는 <<뒤에>>
# center는 값을 가운데두고 <<원하는 문자열을 가운데에>>
# zfill width만큼의 0 을 앞에 붙여줌 zfill(width)

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

# use rjust


def solution2(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i | j)[2:])
        # 2진수화 했을때 두개를 비교하고 하나라도 1일경우 1로 나오게된다
        # ex ) bin(20) => 10100 , bin(1) => 00001 bin(20|1) => 11111
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer


# # ["#####","# # #", "### #", "# ##", "#####"]
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))

# new = bin(20)
# newnew = new + "1"
# print(int(newnew, 2))
