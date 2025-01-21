x = int(input())
boundary  = 1
count = 1
jump = 0

if x == 1:
    print(1)
else:
    while x > boundary:
        count += 1
        jump +=6
        boundary += jump
    print(count)