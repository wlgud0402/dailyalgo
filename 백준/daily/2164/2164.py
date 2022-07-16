import sys
from collections import deque
sys.stdin = open('2164.txt')

max_card_number = int(sys.stdin.readline())

cards = deque()
for num in range(max_card_number, 0, -1):
    cards.append(num)

while len(cards) != 1:
    cards.pop()
    top = cards.pop()
    cards.appendleft(top)

print(cards[-1])
