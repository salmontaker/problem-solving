ans = list()
for n in range(4, int(input()) + 1):
    k = set(str(n))
    if len(k - {"4"}) == 0 or len(k - {"7"}) == 0 or len(k - {"4", "7"}) == 0:
        ans.append(n)
print(ans[-1])
