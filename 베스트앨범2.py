#zip 없이 풀기

def solution(genres, plays):
    plays_count = {}
    answer = []
    genres_plays_sets = list(zip(genres, plays))

    for genres_plays_set in genres_plays_sets:
        key = genres_plays_set[0]
        try:
            if plays_count[key]:
                plays_count[key] += genres_plays_set[1]
        except:
            plays_count[key] = genres_plays_set[1]

    

    return plays_count




print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))