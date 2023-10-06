def is_sequence(arr):
    if len(arr) < 3:
        return True

    diff = arr[0] - arr[1]
    for i in range(1, len(arr) - 1):
        if arr[i] - arr[i + 1] != diff:
            return False

    return True


cnt = 0
for i in range(1, int(input()) + 1):
    if is_sequence(list(map(int, str(i)))):
        cnt += 1

print(cnt)
