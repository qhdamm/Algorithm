city_num = int(input())
street_list = list(map(int, input().split()))
price_list = list(map(int, input().split()))
min_price = price_list[0]
result = 0

for i in range(city_num-1):
    result += min_price*street_list[i]
    if min_price >= price_list[i+1]:
        min_price = price_list[i+1]
print(result)