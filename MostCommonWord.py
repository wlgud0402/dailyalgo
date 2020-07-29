import re
class Solution:
    def mostCommonWord(self, sentence, ban):
        counts = {}
        sentence = sentence.replace(",","")
        sentence = sentence.replace(".","")
        sentence = sentence.replace("!","")

        sentence = sentence.split(" ")
        print(sentence)

        for i in range(len(sentence)):
            key = sentence[i].lower()
            
            if key in ban:
                continue

            if key in counts:
                counts[key] += 1

            else:
                counts[key] = 1


        return max(counts, key=counts.get)


solution = Solution()
print(solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))

print(solution.mostCommonWord("a, a, a, a, b, b, b, c, c" ,["a"]))
        