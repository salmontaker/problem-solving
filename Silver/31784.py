import sys

input = sys.stdin.readline


def get_order(ch):
    return ord(ch) - ord("A")


N, K = map(int, input().split())
S = [*input().strip()]

for i in range(N - 1):
    if S[i] != "A":
        diff = 26 - get_order(S[i])
        if diff <= K:
            S[i] = "A"
            K -= diff


if K > 0:
    S[-1] = chr(ord("A") + (get_order(S[-1]) + K) % 26)

print("".join(S))
