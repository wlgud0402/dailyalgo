import sys
sys.stdin = open('txt/10825_국영수.txt')
students_count = int(sys.stdin.readline())

students = []
for i in range(students_count):
    student_info = sys.stdin.readline().split()
    name = student_info[0]
    ko = int(student_info[1])
    en = int(student_info[2])
    ma = int(student_info[3])
    students.append([name, ko, en, ma])

sorted_students = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for sorted_student in sorted_students:
    print(sorted_student[0])
