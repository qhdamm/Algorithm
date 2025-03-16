import sys

sejun = sys.stdin.readline().strip()

N = 0
index = 0

while True:
    N += 1
    str_N = str(N)

    for char in str_N:
        if index < len(sejun) and sejun[index] == char:
            index += 1
            if index == len(sejun):
                print(N)
                exit()
