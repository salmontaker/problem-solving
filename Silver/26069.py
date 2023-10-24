from collections import defaultdict

people = defaultdict(int)
people["ChongChong"] = 1

for _ in range(int(input())):
    a, b = input().split()
    if people[a]:
        people[b] = 1
    elif people[b]:
        people[a] = 1

print(sum(people.values()))
