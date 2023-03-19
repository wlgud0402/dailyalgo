def solution(n, m, section):
    re_paint_count = 0
    while section:
        check_section = set(section)
        start_section = section[0]
        for i in range(m):
            try:
                if start_section + i in check_section:
                    check_section.remove(start_section + i)
            except:
                return re_paint_count
        else:
            section = sorted(list(check_section))
            re_paint_count += 1

    return re_paint_count


print(solution(8, 4, [2, 3, 6]))  # 2
print(solution(5, 4, [1, 3]))
