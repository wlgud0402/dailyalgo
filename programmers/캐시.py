from collections import deque


def solution(cacheSize, cities):
    cities = [city.lower() for city in cities]
    cash = deque()
    time = 0
    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        flag = True
        if len(cash) < cacheSize and city not in cash:
            time += 5
            cash.append(city)
            continue

        if len(cash) < cacheSize and city in cash:
            time += 1
            cash.remove(city)
            cash.append(city)
            continue

        if city in cash:
            cash.remove(city)
            cash.append(city)
            time += 1
        else:
            cash.popleft()
            cash.append(city)
            time += 5

        for i, v in enumerate(cash):
            if v == city:
                time += 1
                del cash[i]
                cash.append(v)
                flag = False
                break

        if flag:
            time += 5
            cash.popleft()
            cash.append(city)
    return time


print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
                   "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))


def solution2(cacheSize, cities):
    cities = [city.lower() for city in cities]
    cash = deque()
    time = 0
    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        flag = True
        if len(cash) < cacheSize and city not in cash:
            time += 5
            cash.append(city)
            continue

        if len(cash) < cacheSize and city in cash:
            time += 1
            cash.remove(city)
            cash.append(city)
            continue

        if city in cash:
            cash.remove(city)
            cash.append(city)
            time += 1
        else:
            cash.popleft()
            cash.append(city)
            time += 5

    return time
