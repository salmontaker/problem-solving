import sys

input = sys.stdin.readline

BASE36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encode36(n):
    res = []

    while n != 0:
        res.append(BASE36[n % 36])
        n //= 36

    return "".join(reversed(res)) if res else "0"


NUMS = [input().strip() for _ in range(int(input()))]
K = int(input())
DIFF = {digit: 0 for digit in BASE36}

for num in NUMS:
    for exp, base in enumerate(reversed(num)):
        DIFF[base] += (35 - int(base, 36)) * (36**exp)

answer = sum(map(lambda x: int(x, 36), NUMS)) + sum(
    sorted(DIFF.values(), reverse=True)[:K]
)

print(encode36(answer))
