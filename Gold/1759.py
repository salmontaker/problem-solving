import sys
from itertools import combinations

input = sys.stdin.readline
L, C = map(int, input().split())
A = sorted(input().split())

for word in combinations(A, L):
    vowels = 0
    consonants = 0

    for ch in word:
        if ch in ("a", "e", "i", "o", "u"):
            vowels += 1
        else:
            consonants += 1

    if vowels >= 1 and consonants >= 2:
        print("".join(word))
