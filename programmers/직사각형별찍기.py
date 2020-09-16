def solution(width, height):
    for i in range(height):
        for j in range(width):
            print('*', end='')
        print()

solution(5,3)

# width, height = map(int, raw_input().strip().split(' '))

# for i in range(height):
#     print("*" * width)