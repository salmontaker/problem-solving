import sys

input = sys.stdin.readline


def convert(s):
    cnt = [0] * 26
    for c in s:
        cnt[ord(c) - ord("A")] += 1

    return cnt


def check(a, b):
    A, B = convert(a), convert(b)
    diff = 0
    for i in range(26):
        diff += abs(A[i] - B[i])

    return abs(len(a) - len(b)) < 2 and diff < 3


S = [input().strip() for _ in range(int(input()))]
answer = 0
for s in S[1:]:
    answer += check(S[0], s)
print(answer)
