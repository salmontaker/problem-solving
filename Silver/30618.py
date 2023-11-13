N = int(input()) + 1
A = [*range(1, N)]
print(*A[0:N:2], *reversed(A[1:N:2]))
