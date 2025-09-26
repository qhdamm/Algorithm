import sys
input = sys.stdin.readline

list_28 = [2]
list_30 = [4, 6, 9, 11]
list_31 = [1, 3, 5, 7, 8, 10, 12]
day_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

m, d = map(int, input().split())
day = 0
if m > 1:
    for i in range(1, m):
        if i in list_28:
            day += 28
        elif i in list_30:
            day += 30
        else:
            day += 31
day += d
ans = day % 7
print(day_list[ans])
