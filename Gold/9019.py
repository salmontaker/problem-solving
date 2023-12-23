import sys
from collections import deque

input = sys.stdin.readline


def F(n):
    return (n // 1000, n % 1000 // 100, n % 100 // 10, n % 10)


def D(n):
    return (2 * n % 10000, "D")


def S(n):
    return (9999 if n == 0 else n - 1, "S")


def L(n):
    a, b, c, d = F(n)
    return (b * 1000 + c * 100 + d * 10 + a, "L")


def R(n):
    a, b, c, d = F(n)
    return (d * 1000 + a * 100 + b * 10 + c, "R")


for _ in range(int(input())):
    A, B = map(int, input().split())
    queue = deque([(A, "")])
    visited = [0] * 10000
    visited[A] = 1

    while queue:
        now, history = queue.popleft()
        if now == B:
            print(history)
            break
        for next, cmd in [D(now), S(now), L(now), R(now)]:
            if -1 < next < 10000 and not visited[next]:
                queue.append((next, history + cmd))
                visited[next] = 1
