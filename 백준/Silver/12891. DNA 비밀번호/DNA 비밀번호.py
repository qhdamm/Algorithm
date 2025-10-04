import sys

input = sys.stdin.readline
S, P = map(int, input().split())
sequence = [dna for dna in input().strip()]
a_min, c_min, g_min, t_min = map(int, input().split())
acgt_list = [0] * 4
acgt_value = ('A', 'C', 'G', 'T')

window_list = sequence[:P]
acgt_list[0] = window_list.count('A')
acgt_list[1] = window_list.count('C')
acgt_list[2] = window_list.count('G')
acgt_list[3] = window_list.count('T')


def val_num(acgt_list):
    if acgt_list[0] >= a_min and acgt_list[1] >= c_min and acgt_list[2] >= g_min and acgt_list[3] >= t_min:
        return 1
    else:
        return 0

ans = val_num(acgt_list)

for i in range(P, S):
    pop_idx = acgt_value.index(sequence[i-P])
    acgt_list[pop_idx] -= 1
    add_idx = acgt_value.index(sequence[i])
    acgt_list[add_idx] += 1
    ans += val_num(acgt_list)

print(ans)

    
