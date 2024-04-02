import sys

input = sys.stdin.readline

N = int(input())
R = [*map(int, input().split())]
D = [0] * N

# 모든 서로 인접한 두 학생 중 한 명 이상을 고르므로, 한 명이면 고르지 않아도 된다.
D[0] = 0

if N > 1:
    D[1] = min(R[0], R[1])
if N > 2:
    for i in range(2, N):
        # 자신 앞 2명 고르기 vs 자신과 앞사람 고르기
        D[i] = min(D[i - 2] + R[i - 1], D[i - 1] + R[i])

print(D[N - 1])
