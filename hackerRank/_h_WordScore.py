def score_words(words):
	words = words.split(" ")
	
	count = {}

	for i in range(len(words)):
		count[words[i]] = 0
		for spell in words[i]:
			if spell == "a":
				count[words[i]] += 1
				continue
			if spell == "e":
				count[words[i]] += 1
				continue
			if spell == "i":
				count[words[i]] += 1
				continue
			if spell == "o":
				count[words[i]] += 1
				continue
			if spell == "u":
				count[words[i]] += 1
				continue
			if spell == "y":
				count[words[i]] += 1
				continue

	points = list(count.values())
	answer = 0
	for point in points:
		if point % 2 == 0:
			answer += 2
		else:
			answer += 1
	return answer

print(score_words("motmjatlirwxbkqbhkh ujxxfuabn nsgvtsbiexrjww kpcnzkgukfiwwlcptyc rvkhqdudg hjanmpuacpghbbyvax jgavhhhj"))