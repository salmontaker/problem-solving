import sys

input = sys.stdin.readline

F = lambda p1, p2: (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
N, M = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]
X, Y = 0, 0
ANS = 0

for _ in range(M):
    A.sort(key=lambda pos: F(pos, (X, Y)))
    ANS += F(A[-1], (X, Y))
    X, Y = A.pop()
    A.append([*map(int, input().split())])

print(ANS)
