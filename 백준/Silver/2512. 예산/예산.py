import sys

N = int(sys.stdin.readline().strip())
areas = [int(area) for area in sys.stdin.readline().split()]
budget = int(sys.stdin.readline().strip())

if sum(areas) <= budget:
    print(max(areas))
else:
    left, right = 0, max(areas)
    answer = 0

    while left <= right:
        mid = (left+right) //2
        total_budget = sum(min(mid, area) for area in areas)

        if total_budget <= budget:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    print(answer)