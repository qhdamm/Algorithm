import sys
from collections import Counter
input = sys.stdin.readline
num = int(input())

for _ in range(num):
    count = 0
    test = list(map(int, input().split()))
    test_num, students = test[0], test[1:]
    for i in range(20):
        for j in range(i+1, 20):
            if students[i] > students[j]:
                students[i], students[j] = students[j], students[i]
                count += 1
    print(test_num, count)

# method2
# import sys
# from collections import Counter
# input = sys.stdin.readline
# num = int(input())

# for _ in range(num):
#     count = 0
#     line = []
#     test = list(map(int, input().split()))
#     test_num, students = test[0], test[1:]
#     for student in students:
#         position = 0
#         while position < len(line) and line[position] < student:
#             position += 1
#         line.insert(position, student)
#         count += len(line) - position - 1
#     print(test_num, count)
