import sys
from heapq import heappush, heappop

input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    heappush(heap, int(input()))

answer = 0
while len(heap) != 1:
    a, b = heappop(heap), heappop(heap)
    answer += a + b
    heappush(heap, a + b)

print(answer)
