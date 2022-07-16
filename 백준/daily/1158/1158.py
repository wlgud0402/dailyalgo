import sys
from collections import deque

sys.stdin = open('1158.txt')

max_number, jump = map(int, input().split())

numbers = deque([i for i in range(1, max_number+1)])
pop_sequence = []
while numbers:
    numbers.rotate(-jump+1)
    popped = numbers.popleft()
    pop_sequence.append(str(popped))

pop_answer = ', '.join(pop_sequence)
print(f"<{pop_answer}>")
