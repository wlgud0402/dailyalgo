table = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
    "IV":4,
    "IX":9,
    "XL":40,
    "XC":90,
    "CD":400,
    "CM":900
}


class Solution:
    def romanToInt(self, strings):
        result = 0
        skip = False
        for i in range(len(strings)):
            if skip == True:
                skip = False
                continue #skip이 된거라면 continue로 한칸 건너 뛰어줌
            if i != len(strings) - 1:
                s = strings[i] + strings[i + 1]
                if s in table:
                    result += table.get(s)
                    skip = True
                else:
                    result += table.get(strings[i])
            else:
                result += table.get(strings[i])
        return result

solution=Solution()

print(solution.romanToInt("IV"))