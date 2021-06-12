import sys
sys.stdin = open('txt/10814_나이순정렬.txt')
people_count = int(sys.stdin.readline())


persons = []
for i in range(people_count):
    condition = sys.stdin.readline().split()
    persons.append([int(condition[0]), condition[1], i])

sorted_persons = sorted(persons, key=lambda x: (x[0], x[2]))


for person in sorted_persons:
    print(person[0], person[1])
