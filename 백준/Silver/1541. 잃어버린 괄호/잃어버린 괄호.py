expression = input()
no_minus = expression.split('-')
answer_list = []

for part in no_minus:
    plus_x = 0
    plus_part = part.split('+')
    for x in plus_part:
        plus_x += int(x)
    answer_list.append(plus_x)
answer = int(answer_list[0])
for item in answer_list[1:]:
    answer -= int(item)
print(answer)