from heapq import heappop, heappush

N = int(input())
cur = int(input())
answer = 0
heap = []

if N > 1:
    for _ in range(N - 1):
        heappush(heap, -int(input()))

    while cur <= -heap[0]:
        heappush(heap, heappop(heap) + 1)
        cur += 1
        answer += 1

print(answer)
