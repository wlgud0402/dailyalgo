from functools import reduce

arr = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"], ["green_turbansdff", "headgear"], ["red_sunglasses", "eyewear"]]

my_map = {}
def solution(clothes):
    for c_name, c_type in arr:
        if c_type in my_map:
            my_map[c_type] += 1
        else:
            my_map[c_type] = 1

    values = my_map.values()
    return reduce(lambda acc, curr: acc * (curr +1), values, 1)-1

print(solution(arr))
