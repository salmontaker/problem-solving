import sys
from collections import deque

input = sys.stdin.readline


def atoi(ch):
    return ord(ch) - ord("a")


def bfs(start, target):
    Q = deque([start])
    while Q:
        current = Q.popleft()
        if current == target:
            return True

        for next in G[current]:
            Q.append(next)

    return False


G = [[] for _ in range(26)]

for _ in range(int(input())):
    a, _, b = input().split()
    G[atoi(a)].append(atoi(b))

for _ in range(int(input())):
    a, _, b = input().split()
    print("T" if bfs(atoi(a), atoi(b)) else "F")
