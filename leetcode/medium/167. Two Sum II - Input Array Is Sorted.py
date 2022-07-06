class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #         # O(n2)
        #         for i in range(len(numbers)-1):
        #             for j in range(i+1, len(numbers)):
        #                 if numbers[i] + numbers[j] == target:
        #                     return [i+1,j+1]

        # 딕셔너리 활용 방법
        # O(n)
        possible_target = {}
        for i, v in enumerate(numbers):
            if target - v in possible_target.keys():
                return [possible_target[target - v]+1, i + 1]
            else:
                possible_target[v] = i

        # 투포인터 활용 방법 => 이미 정렬되어있다면 n
        # # O(n)
        # left_point = 0
        # right_point = len(numbers)-1
        # for i in range(len(numbers)):
        #     if numbers[left_point] + numbers[right_point] == target:
        #         return [left_point+1, right_point+1]

        #     if numbers[left_point] + numbers[right_point] > target:
        #         right_point -= 1
        #         continue
        #     else:
        #         left_point += 1
