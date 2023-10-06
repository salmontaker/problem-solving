for _ in range(int(input())):
    input()
    n = sorted(list(input()), reverse=True)
    i = len(n) - 1
    print(int("".join(n[:i])) + int(n[i]))
