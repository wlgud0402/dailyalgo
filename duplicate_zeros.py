#리턴없이 원래 arr를 바꾸기
#원래 길이 초과할수 x
import copy
class Solution:
    # def duplicateZeros(self, numbers):
    #     length = len(numbers)
    #     zero_idx = []
    #     for i, num in enumerate(numbers):
    #         if num == 0:
    #             zero_idx.append(i)
        
    #     for zero in zero_idx:
    #         numbers.insert(zero+1, 0)

    #     numbers = numbers[:length]
    #     print(numbers)

    def duplicateZeros2(self, numbers):
        length = len(numbers)
        answer = []
        for i in range(len(numbers)):
            if numbers[i] == 0:
                  answer.append(0)
                  answer.append(0)
            else :
                answer.append(numbers[i])

        count = 0
        for i in range(len(answer)):
            if count < len(numbers):
                  numbers[i] = answer[i]
            count = count +1
        
        # numbers = answer[:length]
        print(numbers)
        

#[1,0,0,2,3,0,0,4]


solution = Solution()
print(solution.duplicateZeros2([1,0,2,3,0,4,5,0]))