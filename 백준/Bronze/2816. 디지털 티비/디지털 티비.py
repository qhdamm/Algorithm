num = int(input())
channel = [input() for i in range(num)]
KBS1_index = channel.index('KBS1')
print('1'*KBS1_index+'4'*KBS1_index, end='')
if KBS1_index < channel.index('KBS2'):
    KBS2_index = channel.index('KBS2')
else:
    KBS2_index = channel.index('KBS2') + 1
print('1' * KBS2_index+'4'*(KBS2_index-1))