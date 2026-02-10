import sys

input = sys.stdin.readline
n = int(input())
start = list(map(int, input().strip()))
target = list(map(int, input().strip()))


def switch(idx, arr):
    for i in (idx-1, idx, idx+1):
        if 0<= i < n:
            arr[i] = 1 - arr[i]

ans1 = 1
arr1 = start[:]
switch(0, arr1)
for i in range(1, n):
    if arr1[i-1] != target[i-1]:
        switch(i, arr1)
        ans1 += 1

ans2 = 0
arr2 = start[:]
for i in range(1, n):
    if arr2[i-1] != target[i-1]:
        switch(i, arr2)
        ans2 += 1

if arr1 == target and arr2 == target:
    print(min(ans1, ans2))
elif arr1 != target and arr2 != target:
    print(-1)
else:
    print(ans1 if arr1==target else ans2)