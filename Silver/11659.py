import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr, s = [0], 0
for _ in list(map(int, input().split())):
    arr.append(s + _)
    s += _
for _ in range(m):
    i, j = map(int, input().split())
    print(arr[j] - arr[i - 1])
