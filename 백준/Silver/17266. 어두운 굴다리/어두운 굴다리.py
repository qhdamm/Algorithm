import math
street = int(input())
num = int(input())
where = list(map(int, input().split()))
result = max(where[0], street-where[-1])
for i in range(len(where)-1):
    test_case = math.ceil((where[i+1] - where[(i)])/2)
    if result <= test_case:
        result = (test_case)
print(result)