class Solution:
    def toGoatLatin(self, S):
        S = S.split(" ")
        answer = ""
        for i in range(len(S)):

            new_S = S[i]
            if new_S.startswith("a") or new_S.startswith("e") or new_S.startswith("i") or new_S.startswith("o") or new_S.startswith("u") or new_S.startswith("A") or new_S.startswith("E") or new_S.startswith("I") or new_S.startswith("O") or new_S.startswith("U"):
                new_S += "ma"
            else:
                new_S = S[i][1:] + S[i][0]
                new_S += "ma"

            new_S += "a" * (i+1)
            answer += new_S + " "
        return answer[:-1]

solution = Solution()
print(solution.toGoatLatin("I speak Goat Latin"))