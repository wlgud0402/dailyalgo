from itertools import product
import itertools

def solution(numbers, target):
    answer = 0
    # minus_list = [int("-" + str(num)) for num in numbers]
    # plus_list = [int("+" + str(num)) for num in numbers]

    minus_list = []
    plus_list = []

    combinations = [minus_list, plus_list]

    combi = [minus_list,minus_list,minus_list,minus_list,minus_list,plus_list,plus_list,plus_list,plus_list,plus_list,]

    for num in numbers:
        minus_list.append(int("-"+str(num)))
        plus_list.append(int("+"+str(num)))

    solve = list(product(*combinations))
    solve2 = list(product(minus_list, plus_list, repeat=2))
    solve3 = list(product(*combi))

    return solve3

print(solution([1, 1, 1, 1, 1],3))
print()
print()
import itertools
print(list(itertools.product(["-", "+"], repeat = 2)))
print()
print(list(itertools.permutations(["-", "+"], 2)))
print()
print(list(itertools.combinations(["-", "+"], 2)))


