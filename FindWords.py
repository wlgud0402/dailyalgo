"""
1) char_map.... a몇개 b몇개 ... ( 갯수카운팅 )

2) 반복문 돌리는 녀석을 remove하면 꼬임

3) 의미없는 리스트컴프리헨션 "abc"    ["a", "b", "c"]
"""
import copy
class Solution:
    def countCharacters(self, words, chars):
        count = {}
        answer = 0
        #count 로 chars의 철자별 갯수를 세줌
        for char in chars:
            try:   
                count[char] += 1
            except:
                count[char] = 1 
        #words의 word에서 반복문을 돌아 철자별로 확인해서 있는 것들을 count딕셔너리에서 빼줌       
        for word in words:
            count_copy = copy.deepcopy(count)
            flag = True
            for c in word:
                try:
                    if count_copy[c] == 0:
                        flag = False
                        break
                    if count_copy[c] >= 1:
                        count_copy[c] -= 1
                except:
                    flag = False
                    break
            if flag:
                answer += len(word)
        return answer
                
solution=Solution()
print(solution.countCharacters(["cat","bt","hat","tree","atachhhhhh"],"atach"))
print(solution.countCharacters(["hello","world","leetcode"],"welldonehoneyr"))
