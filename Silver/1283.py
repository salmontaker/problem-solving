import sys

input = sys.stdin.readline

answer = []
used = set()


def can_assign_head(option):
    head = option[0]
    for i in range(len(option)):
        if head.upper() not in used:
            answer.append(option[0:i] + f"[{head}]" + option[i + 1 :])
            used.add(head.upper())
            return True
        if option[i] == " ":
            head = option[i + 1]

    return False


def can_assign_any(option):
    for i in range(len(option)):
        if option[i] != " " and option[i].upper() not in used:
            answer.append(option[0:i] + f"[{option[i]}]" + option[i + 1 :])
            used.add(option[i].upper())
            return True

    return False


for option in [input().strip() for _ in range(int(input()))]:
    if can_assign_head(option):
        continue

    if can_assign_any(option):
        continue

    answer.append(option)

print("\n".join(answer))
