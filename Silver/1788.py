# 파이썬에서의 음수 나머지 연산 : https://stackoverflow.com/questions/3883004
def mod(n, base):
    return n - int(n / base) * base


N = int(input())
offset = -1 if N < 0 else 1

N = abs(N)
F = [0, 1] + [0] * N

# N이 양수일 경우 : F[i] = F[i-2] + F[i-1]
# N이 음수일 경우 : F[i] = F[i-2] - F[i-1]
for i in range(2, N + 1):
    F[i] = mod(F[i - 2] + F[i - 1] * offset, 10**9)

ans = F[N]
print(0 if ans == 0 else 1 if ans > 0 else -1)
print(abs(ans))
