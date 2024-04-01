import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
C = Counter(map(int, input().split()))

for key in sorted(C.keys()):
    if C[key * 2]:
        C[key * 2] += C[key]
        C[key] = 0

print(C.most_common()[0][1])
