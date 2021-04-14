# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import Counter

T = int(sys.stdin.readline())
shoe_size = sys.stdin.readline().split()
count = Counter(shoe_size)
people = int(sys.stdin.readline())

answer = 0
for _ in range(people):
    size, price = sys.stdin.readline().split()
    if count.get(size) != 0 and count.get(size):
        count[size] -= 1
        answer += int(price)
print(answer)
