import sys
from heapq import heapify, heappush, heappop

input = sys.stdin.readline

N, H, T = map(int, input().split())
K = 0
A = [-int(input()) for _ in range(N)]
heapify(A)

while True:
    tallest = -heappop(A)
    if tallest < H:
        print("YES", K, sep="\n")
        break
    else:
        if K == T:
            print("NO", tallest, sep="\n")
            break

        heappush(A, -tallest if tallest == 1 else -(tallest // 2))
        K += 1
