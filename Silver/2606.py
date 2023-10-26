from collections import deque


def bfs(start):
    queue = deque([start])
    visited[start] = True
    cnt = 0

    while queue:
        q = queue.popleft()
        cnt += 1
        for i in range(1, N + 1):
            if matrix[q][i] and not visited[i]:
                queue.append(i)
                visited[i] = True

    # 1번 컴퓨터를 제외한 컴퓨터의 수
    return cnt - 1


N = int(input())
matrix = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(int(input())):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = True

print(bfs(1))
