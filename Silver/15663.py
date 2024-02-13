import sys

input = sys.stdin.readline


def dfs(depth):
    if depth == M:
        print(*S[:M])
        return

    last = 0
    for i in range(N):
        if not V[i] and last != A[i]:
            S[depth] = A[i]
            last = A[i]

            V[i] = 1
            dfs(depth + 1)
            V[i] = 0


N, M = map(int, input().split())
A = sorted(map(int, input().split()))
S = [0] * 10
V = [0] * 10

dfs(0)

# from itertools import permutations

# N, M = map(int, input().split())
# A = sorted(map(int, input().split()))

# for p in dict.fromkeys(permutations(A, M)):
#     print(*p)
