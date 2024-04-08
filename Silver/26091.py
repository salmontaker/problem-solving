import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = sorted(map(int, input().split()))

answer = 0
left = 0
right = N - 1

while left < right:
    if A[left] + A[right] >= M:
        answer += 1
        left += 1
        right -= 1
    else:
        left += 1

print(answer)
