import sys

input = sys.stdin.readline

L = int(input())
A = [0] + [*map(int, input().split())]
B = [0] * (L + 1)

for i in range(1, L + 1):
    for j in range(1, L // i + 1):
        B[i] += A[i * j]

answer = [0, 0]
for idx, value in enumerate(B[1:]):
    if answer[1] < value:
        answer[0] = idx + 1
        answer[1] = value

print(*answer)
