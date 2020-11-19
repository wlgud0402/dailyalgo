
def electionsWinners(votes, k):
    # count = 0
    # for i, v in enumerate(votes):
    #     now = v + k
    #     try:
    #         left_max = max(votes[:i])
    #     except:
    #         left_max = 0

    #     try:
    #         right_max = max(votes[i+1:])
    #     except:
    #         right_max = 0

    #     all_max = max(left_max, right_max)

    #     if now > all_max:
    #         count += 1

    # return count


print(electionsWinners([3, 1, 1, 3, 1], 2))  # winners count = 2 ([3, 3])
