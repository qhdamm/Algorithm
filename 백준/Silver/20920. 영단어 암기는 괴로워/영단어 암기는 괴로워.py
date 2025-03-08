from collections import Counter
import sys

N, M = map(int, sys.stdin.readline().split())
words = [sys.stdin.readline().strip() for _ in range(N)]
counts = Counter(words)
long_words = [word for word in counts if len(word) >= M]
sorted_words = sorted(long_words, key=lambda word: (-counts[word], -len(word), word))
for word in sorted_words:
    print(word)
