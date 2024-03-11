import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
S = [*map(int, input().split())]
answer = 0

for combo in combinations(range(1, 10), 2):
    cnt = 0
    for s in S:
        if s in combo:
            cnt += 1
            if cnt > answer:
                answer = cnt
        else:
            cnt = 0

print(answer)