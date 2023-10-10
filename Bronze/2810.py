n = int(input())
s = input()
cnt = [s.count("S"), s.count("LL")]
print(n if n in cnt else cnt[0] + cnt[1] + 1)
