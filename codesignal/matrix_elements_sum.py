#stack 의 구조를 활용함

def matrixElementsSum(matrix):
    stacks = [matrix[0]]

    for i in range(1 ,len(matrix)):
        add = []
        for j in range(len(matrix[i])):
            if stacks[-1][j] == 0:
                add.append(0)
            else:
                add.append(matrix[i][j])
        stacks.append(add)

    answer = 0
    for stack in stacks:
        answer += sum(stack)

    return answer