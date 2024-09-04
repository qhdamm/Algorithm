n = int(input())
wait_time = 0
numbers = input().split()
list = [int(num) for num in numbers]
wait_list = []

while len(list) > 0:
    smallest = min(list)
    wait_time += smallest
    wait_list.append(wait_time)
    list.remove(smallest)
print(sum(wait_list))