def d(num):
    result = num
    str_num = str(num)
    for n in str_num:
        result += int(n)
    return result
    

list_10000 = [False]*10000

for i in range(1, 10001):
    num = d(i)
    if num <= 10000:
        list_10000[num-1] = True

for i in range(10000):
    if list_10000[i] == False:
        print(i+1)
    