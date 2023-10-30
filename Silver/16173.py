from collections import deque


def bfs(y, x):
    queue = deque([(y, x)])
    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (0, 1)]:
            Y, X = y + dy * board[y][x], x + dx * board[y][x]
            if Y < N and X < N:
                if board[Y][X] == -1:
                    return True
                elif board[Y][X] == 0:
                    continue
                else:
                    queue.append((Y, X))

    return False


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print("HaruHaru" if bfs(0, 0) else "Hing")
