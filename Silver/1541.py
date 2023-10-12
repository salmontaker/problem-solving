def calc(x: str):
    return sum(map(int, x.split("+")))


n = input().split("-")
print(calc(n[0]) - sum(calc(_) for _ in n[1:]))
