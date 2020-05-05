def isOdd_Even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(isOdd_Even(10))

list_x=[[1,2],[2,3]]
list_y=[[3,4],[5,6]]

def double_list(list_x, list_y):
    answer=[]
    x_1 = list_x[0]
    x_2 = list_x[1]

    y_1 = list_y[0]
    y_2 = list_y[1]

    zip_1 = [x+y for x,y in zip(x_1, y_1)]
    zip_2 = [x+y for x,y in zip(x_2, y_2)]

    answer.append(zip_1)
    answer.append(zip_2)

    return answer

print(double_list(list_x, list_y))


A=[[1,2,3],[2,3,4]]
B=[[3,4,5],[5,6,6]]

def Matrix(A,B):
    answer = [[a + b for a, b in zip(A_1, B_1)] for A_1, B_1 in zip(A,B)] 
    return answer

print(Matrix(A,B))

def sumMatrix(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j] 
    return A


