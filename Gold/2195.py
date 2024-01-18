import sys

input = sys.stdin.readline

S = input().strip()
P = input().strip()

answer = 1
left, right = 0, 0
while right < len(P):
    target = P[left : right + 1]
    if S.find(target) == -1:
        left = right
        answer += 1
    right += 1

print(answer)
