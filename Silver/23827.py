a = [*map(int, [*open(0)][1].split())]
s = sum(a)
r = 0
for n in a:
    s -= n
    r = r + n * s
print(r % (10**9 + 7))
