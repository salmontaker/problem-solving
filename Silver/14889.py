import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
S = [[*map(int, input().split())] for _ in range(N)]
row_sum = [sum(row) for row in S]
col_sum = [sum(col) for col in zip(*S)]
powers = [i + j for i, j in zip(row_sum, col_sum)]
total = sum(row_sum)

answer = 10**9
for combo in combinations(powers, N // 2):
    answer = min(answer, abs(total - sum(combo)))

print(answer)
