
def electionsWinners(votes, k):
    votes.sort()
    count = 0
    if votes[-1]+k > votes[-2]:
        count += 1
    for i in range(len(votes)-1):
        if votes[i] + k > votes[-1]:
            count += 1
    return count


print(electionsWinners([5, 1, 3, 4, 1], 0))  # 1
