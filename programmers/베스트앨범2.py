# zip 없이 풀기


def solution(genres, plays):
    play_count = {}
    index = [i for i in range(len(genres))]
    # zip을통해 장르와 플레이수를 묶어주기
    genres_plays_sets = list(zip(genres, plays, index))
    print("장르플레이카운츠: ", genres_plays_sets)

    # key가 hash에 들었는지 확인하고 값을 설정하거나 더해줌
    for genres_plays_set in genres_plays_sets:
        key = genres_plays_set[0]
        value = genres_plays_set[1]

        if key in play_count:
            play_count[key] += value
        else:
            play_count[key] = value

    # 만들어진 딕셔너리의 값을 기준으로 정렬
    sorted_play_count = sorted(
        play_count.items(), key=(lambda x: x[1]), reverse=True)
    print("값을 기준으로 정렬한 플레이횟수: ", sorted_play_count)

    genres_plays_sets.sort(key=lambda element: element[1])
    print("값을 기준으로 정렬된 zip: ", genres_plays_sets)

    # answer = []
    # for i in range(len(sorted_play_count)):
    #     count = 0
    #     for j in range(len(genres_plays_sets)):
    #         if


print(solution(["classic", "pop", "classic",
                "classic", "pop"], [500, 600, 150, 800, 2500]))

# 4,1,3,0
# 집으로 묶기
# 토탈카운트가 많은순서대로 2개씩 뽑아서
# 인덱스에 추가
