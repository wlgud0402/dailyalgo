from itertools import permutations


def solution1(babblings):
    can_babbling_count = 0
    for babbling in babblings:
        print("before", babbling)
        while True:
            before_babbling_length = len(babbling)
            babbling = babbling.replace('aya', '')
            if before_babbling_length == len(babbling):
                break

        while True:
            before_babbling_length = len(babbling)
            babbling = babbling.replace('ye', '')
            if before_babbling_length == len(babbling):
                break

        while True:
            before_babbling_length = len(babbling)
            babbling = babbling.replace('woo', '')
            if before_babbling_length == len(babbling):
                break

        while True:
            before_babbling_length = len(babbling)
            babbling = babbling.replace('ma', '')
            if before_babbling_length == len(babbling):
                break

        if len(babbling) == 0:
            can_babbling_count += 1

    return can_babbling_count


def solution(babblings):
    can_babbling_count = 0
    can_babbling_words = ["aya", "ye", "woo", "ma"]
    all_can_babbling_words_permutations = set()

    for i in range(1, len(can_babbling_words)+1):
        for j in permutations(can_babbling_words, i):
            all_can_babbling_words_permutations.add(''.join(j))

    for babbling in babblings:
        if babbling in all_can_babbling_words_permutations:
            can_babbling_count += 1

    return can_babbling_count


print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
