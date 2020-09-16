import copy
class Solution:
    def maximum69Number (self, num):
        answers = [num]
        
        for i in range(len(str(num))):
            copy_num = copy.deepcopy(num)
            if str(copy_num)[i] == "6":
                copy_num = str(copy_num)[:i] + "9" + str(copy_num)[i+1:]
                answers.append(int(copy_num))
                continue
            if str(copy_num)[i] == "9":
                copy_num = str(copy_num)[:i] + "6" + str(copy_num)[i+1:]
                answers.append(int(copy_num))
                continue

        return max(answers)




solution = Solution()
print(solution.maximum69Number(9999))

# 6669 9969  9699 9666
        