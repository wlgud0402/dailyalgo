# 나눠줘야할 거스름돈 change
# 가능한 거스름돈 500원, 100원, 50원 10원
def solution(change):
    coin_count = 0
    while change != 0:
        if change >= 500:
            change -= 500
            coin_count += 1
            continue

        elif change >= 100:
            change -= 100
            coin_count += 1
            continue

        elif change >= 50:
            change -= 50
            coin_count += 1
            continue

        else:
            change -= 10
            coin_count += 1
            continue

    return coin_count


print(solution(1260))
