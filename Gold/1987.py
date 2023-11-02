import sys

input = sys.stdin.readline


def bfs(y, x):
    queue = set([(y, x, board[y][x])])
    ans = 1

    while queue:
        y, x, visited = queue.pop()

        for dy, dx in delta:
            Y, X = y + dy, x + dx
            if -1 < Y < R and -1 < X < C and board[Y][X] not in visited:
                queue.add((Y, X, visited + board[Y][X]))
                ans = max(ans, len(visited) + 1)

    return ans


R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

print(bfs(0, 0))
