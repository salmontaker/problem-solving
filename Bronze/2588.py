a = int(input())
b = int(input())

for i in list(str(b))[::-1]:
    print(a * int(i))
print(a * b)
