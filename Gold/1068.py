import sys

input = sys.stdin.readline


def dfs(node):
    global answer

    V[node] = 1

    if G[node] == []:
        answer += 1
    else:
        for next in G[node]:
            if not V[next]:
                dfs(next)


N = int(input())
A = [*map(int, input().split())]
K = int(input())

G = [[] for _ in range(N)]
V = [0] * N
root = -1
answer = 0

for i in range(N):
    if A[i] == -1:
        root = i
    elif i != K:
        G[A[i]].append(i)

# 루트 노드가 제거 되었을경우.
if root != K:
    dfs(root)

print(answer)
