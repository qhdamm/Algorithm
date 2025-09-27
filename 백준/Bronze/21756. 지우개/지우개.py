N = int(input())

num_list = [i+1 for i in range(N)]

while len(num_list) > 1:
    new_list = []
    for i in range(len(num_list)):
        if i % 2 == 1:
            new_list.append(num_list[i])
    num_list = new_list

print(*num_list)