import sys
input = sys.stdin.readline

target = input()
t1 = t2 = t3 = t4 = None
if "U" in target:
    t1 = target.index("U")
if t1 is not None and "C" in target[t1:]:
    t2 = t1 + target[t1:].index("C")
if t2 is not None and "P" in target[t2:]:
    t3 = t2 + target[t2:].index("P")
if t3 is not None and "C" in target[t3:]:
    t4 = t3 + target[t3:].index("C")

if t4 is None:
    print("I hate UCPC")
else:
    print("I love UCPC")