
def electionsWinners(votes, k):
    count = 0
    for i, v in enumerate(votes):
        now = v + k
        # print(now)
        if now > max(votes) and votes.count(now) == 0:
            count += 1
            # new_votes = [vote for vote in votes]
            # new_votes[i] = now
            # if now == max(new_votes) and new_votes.count(now) == 1:
            #     count += 1

    return count


print(electionsWinners([3, 1, 1, 3, 1], 2))  # winners count = 2 ([3, 3])
