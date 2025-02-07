num, type = input().split()
unique = set()
for i in range(int(num)):
    person = input()
    if person not in unique:
        unique.add(person)
if type == 'Y':
    print(len(unique))
elif type == 'F':
    print(len(unique)//2)
elif type == 'O':
    print(len(unique)//3)