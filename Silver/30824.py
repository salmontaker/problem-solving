import sys

input = sys.stdin.readline

f = [0, 1, 1] + [0] * 77
for i in range(3, len(f)):
    f[i] = f[i - 1] + f[i - 2]

sums = [set(), set(), set()]
for i in range(1, len(f)):
    sums[0].add(f[i])
    for j in range(1, len(f)):
        sums[1].add(f[i] + f[j])
        for k in range(1, len(f)):
            sums[2].add(f[i] + f[j] + f[k])

for _ in range(int(input())):
    n, target = map(int, input().split())
    print("YES" if target in sums[n - 1] else "NO")
