import sys

input = sys.stdin.readline

N, K, T = map(int, input().split())
S = sorted(map(int, input().split()))
stack = []

for shark in S:
    if T <= shark:
        while stack and K:
            T += stack.pop()
            K -= 1
            if T > shark:
                break

    if T > shark:
        stack.append(shark)

while stack and K:
    T += stack.pop()
    K -= 1

print(T)
