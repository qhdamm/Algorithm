in_list = input().upper()

from collections import Counter
result = Counter(in_list)
count = result.most_common()
if len(count) > 1 and count[0][1] == count[1][1]:
    print('?')
else:
    print(count[0][0])