m, n = map(int, input().split())
p = [False, False] + [True] * (n - 1)

for i in range(2, int(n**0.5) + 1):
    # i가 소수일 경우
    if p[i]:
        # i를 제외한 i의 배수들은 소수가 아님.
        for j in range(i + i, n + 1, i):
            p[j] = False

for i in range(m, n + 1):
    if p[i]:
        print(i)
