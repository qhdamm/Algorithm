import sys

x = sys.stdin.read().splitlines()
vowels = 'aeiou'

for sample in x:
    sample_list = [1 if i in vowels else 0 for i in sample]
    if sample == "end":
        break
    if 1 not in sample_list:
        print(f"<{sample}> is not acceptable.")
        continue
    if any(sample_list[i:i+3] == [0, 0, 0] for i in range(len(sample_list) - 2)) or any(sample_list[i:i+3] == [1, 1, 1] for i in range(len(sample_list) - 2)):
        print(f"<{sample}> is not acceptable.")
        continue
    if any(sample[i]==sample[i+1] and sample[i:i+2] not in ['ee','oo'] for i in range(len(sample)-1)):
        print(f"<{sample}> is not acceptable.")
        continue
    
    print(f"<{sample}> is acceptable.")
