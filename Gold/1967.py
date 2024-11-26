import sys

input = sys.stdin.readline


def dfs(node):
    stack = [(node, 0)]
    visited = [-1] * (N + 1)

    while stack:
        node, dist = stack.pop()

        if visited[node] == -1:
            visited[node] = dist

        for next, weight in reversed(G[node]):
            if visited[next] == -1:
                stack.append((next, dist + weight))

    return visited


N = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    num, child, weight = map(int, input().split())
    G[num].append((child, weight))
    G[child].append((num, weight))

FAR = dfs(1)
print(max(dfs(FAR.index(max(FAR)))))
