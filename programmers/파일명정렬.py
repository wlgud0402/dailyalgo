def solution(files):
    file_comb = []
    for i, v in enumerate(files):
        string_key = ""
        string_flag = True
        number_key = ""

        for j in range(len(v)):
            if not string_flag and (v[j].isalpha() or v[j] == ' ' or v[j] == '.' or v[j] == '-'):
                break

            if string_flag and (v[j].isalpha() or v[j] == ' ' or v[j] == '.' or v[j] == '-'):
                string_key += v[j].lower()
                continue

            if v[j].isdigit():
                number_key += v[j]
                string_flag = False

        number_key = int(number_key.lstrip("0"))
        file_comb.append([string_key, number_key, v, i])
    order = sorted(file_comb, key=lambda x: (x[0], x[1]))

    answer = [file[2] for file in order]
    return answer


print(solution(["img12.png", "img10.png", "img02.png",
                "img1.png", "IMG01.GIF", "img2.JPG"]))

print(solution(["MUZI1.txt", "muzi001.txt", "muzi1.TXT"]))

# ["img1.png", "IMG01.GIF", "img02.png",
# "img2.JPG", "img10.png", "img12.png"]

# aa = "00010100"
# bb = aa.lstrip("0") => 10100

# f = sorted(e, key = lambda x : (x[0], -x[1]))
