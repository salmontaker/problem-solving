import sys

input = sys.stdin.readline

A = int(input())
X = bin(int(input()))[2:]

MOD = 10**9 + 7
D = [A % MOD] + [0] * (len(X) - 1)
for i in range(1, len(D)):
    D[i] = D[i - 1] * D[i - 1] % MOD

answer = 1
for i in range(len(D)):
    if X[i] == "1":
        answer = answer * D[len(D) - i - 1] % MOD

print(answer)
