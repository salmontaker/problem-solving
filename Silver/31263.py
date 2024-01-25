import sys

input = sys.stdin.readline

N = int(input())
S = input().strip()
answer = 0

i = N
while i > 2:
    if S[i - 3] != "0" and S[i - 3 : i] < "642":
        i -= 3
    elif S[i - 2] != "0":
        i -= 2
    else:
        i -= 1

    answer += 1

if i != 0:
    answer += 1

print(answer)
