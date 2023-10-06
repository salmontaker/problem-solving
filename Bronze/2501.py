n, k = map(int, input().split())
d = [i for i in range(1, n + 1) if n % i == 0]
print(d[k - 1] if len(d) >= k else 0)
