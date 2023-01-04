# 1. 귤 고르기 ( 구현문제입니다 )
from collections import Counter


def solution(k, tangerine):
    # 귤의 크기를 key로 갖고 갯수를 세어 dict를 생성합니다
    fruit_map = Counter(tangerine)

    # 갯수를 기준으로 내림차순으로 정랼한 key,value 배열을 생성합니다.
    sorted_fruit_items = sorted(
        fruit_map.items(), key=lambda item: item[1], reverse=True)

    kind = 0
    for fruit_item in sorted_fruit_items:
        # k개를 모두 고른 경우 for문 break
        if k <= 0:
            break

        # 현재 확인하는 귤의 갯수를 최대로 사용해야 종류를 가장 적게 고를 수 있으므로 갯수를 모두 빼줍니다.
        # 종류를 +1 해줍니다
        k -= fruit_item[1]
        kind += 1

    return kind
