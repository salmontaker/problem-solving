n, k = map(int, input().split())
people = [str(i) for i in range(1, n + 1)]
answer = list()
idx = 0

while len(people) > 0:
    idx = (idx + k - 1) % len(people)
    answer.append(people.pop(idx))

print("<" + ", ".join(answer) + ">")
