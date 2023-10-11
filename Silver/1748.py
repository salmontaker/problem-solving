a = 0
n = int(input())
l = len(str(n))

a += (n - 10 ** (l - 1) + 1) * l
for i in range(l - 1):
    a += 9 * 10**i * (i + 1)

print(a)
