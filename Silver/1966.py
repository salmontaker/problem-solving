from collections import deque

for _ in range(int(input())):
    n, k = map(int, input().split())
    queue = deque(map(lambda x: (x[0], x[1]), enumerate(input().split())))
    while len(queue) != 0:
        if queue[0][1] >= max(queue, key=lambda x: x[1])[1]:
            if queue.popleft()[0] == k:
                print(n - len(queue))
                break
        else:
            queue.append(queue.popleft())
