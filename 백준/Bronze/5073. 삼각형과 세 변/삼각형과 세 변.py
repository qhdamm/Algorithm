while True:
    a, b, c = list(map(int, input().split(' ')))
    if a==b==c==0:
        break
    if max((a,b,c))>=sum((a,b,c))-max((a,b,c)):
        print('Invalid')
    elif a==b==c:
        print('Equilateral')
    elif a != b and b!= c and a!=c:
        print('Scalene')
    else:
        print('Isosceles')