coin_list = [500, 100, 50, 10, 5, 1]
price = int(input())
money = 1000 - price
output = 0
for coin in coin_list:
    if money >= coin: 
        output += (money//coin)
        money = money % coin
print(output)