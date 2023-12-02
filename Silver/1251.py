S = input()
L = len(S)
A = "z" * L

for i in range(L - 2):
    for j in range(i + 1, L - 1):
        NEW_S = "".join(
            [*reversed(S[: i + 1])]
            + [*reversed(S[i + 1 : j + 1])]
            + [*reversed(S[j + 1 :])]
        )
        if A > NEW_S:
            A = NEW_S

print(A)
