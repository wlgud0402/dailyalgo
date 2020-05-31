"""
1) char_map.... a몇개 b몇개 ... ( 갯수카운팅 )

2) 반복문 돌리는 녀석을 remove하면 꼬임

3) 의미없는 리스트컴프리헨션 "abc"    ["a", "b", "c"]
"""

class Solution:
    def countCharacters(self, words, chars):
        chars = [char for char in chars]

        can_make_words = []
        count = {}

        for word in words:
            word = [spell for spell in word]
            can_make = True
            for i in range(len(word)):
                if word[i] not in chars:
                    can_make = False
                    break
            if can_make:
                can_make_words.append(word)
        
        return len(sum(can_make_words, []))
                


solution=Solution()

print(solution.countCharacters(["cat","bt","hat","tree"],"atach"))

"atachaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

print(solution.countCharacters(["hello","world","leetcode"],"welldonehoneyr"))
#출력 atach 로 cat과 hat을 만들수 있따 3글자 + 3글자 => 6

