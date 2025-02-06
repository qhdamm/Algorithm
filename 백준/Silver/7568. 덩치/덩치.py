num = int(input())
people_list = []
people_list = [list(map(int, input().split())) for _ in range(num)]
for i in range(num):
    bigger = 0
    for j in range(num):
        if i==j:
            continue
        else:
            if people_list[i][0] < people_list[j][0] and people_list[i][1] < people_list[j][1]:
                bigger += 1
    print(bigger+1, end=" ")
