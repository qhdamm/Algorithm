n = int(input())

pal1=0; pal2=0; leg1=0; leg2=0; huri=0
cookie=[]
head=False

for _ in range(n):
    cookie.append(list(input()))

for i in range(n):
    for j in range(n):
        if cookie[i][j] == '*':
            head=True
            head_x = i+2; head_y = j+1
            print(head_x, head_y)
    if head == True:
        break

for i in range(head_x-1,head_x):
    for j in range(0,head_y-1):
        if cookie[i][j]=="*":
            pal1+=1
    for j in range(head_y,n):
        if cookie[i][j]=='*':
            pal2+=1

for i in range(head_x, n):
    if cookie[i][head_y-1] == "*":
        huri +=1

for i in range(head_x+huri, n):
    for j in range(0, head_y):
        if cookie[i][j]=="*":
            leg1+=1
    for j in range(head_y,n):
        if cookie[i][j]=='*':
            leg2+=1
print(pal1, pal2, huri, leg1, leg2)