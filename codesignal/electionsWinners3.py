
def electionsWinners(votes, k):
    votes.sort()
    len_votes = len(votes)
    max_vote = max(votes)
    count = 0
    for i, v in enumerate(votes):
        if v + k > max_vote:
            count += 1
    return count
    # votes.sort()
    # len_votes = len(votes)
    # print(votes, len_votes)
    # for i, v in enumerate(votes):
    #     if v + k > max(votes):
    #         return len_votes - i

    # return 0


print(electionsWinners([1, 1, 1, 1], 0))
