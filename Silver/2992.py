import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
for n in map(lambda x: int("".join(x)), permutations(sorted(str(N)))):
    if n > N:
        print(n)
        exit()

print(0)
