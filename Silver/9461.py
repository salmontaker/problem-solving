import sys

input = sys.stdin.readline

DP = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90
for i in range(11, len(DP)):
    DP[i] = DP[i - 5] + DP[i - 1]

for _ in range(int(input())):
    print(DP[int(input())])
