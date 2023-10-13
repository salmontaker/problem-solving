n, m = map(int, input().split())
s = {input() for _ in range(n)}
print(sum(1 for _ in range(m) if input() in s))
