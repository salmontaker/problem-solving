class Stack:
    def __init__(self):
        self.stack = []
        self.history = []
        self.max_value = 0

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, value):
        if self.max_value < value:
            self.max_value = value

        self.history.append("+")
        self.stack.append(value)

    def pop(self):
        self.history.append("-")
        return self.stack.pop()

    def top(self):
        return self.stack[len(self.stack) - 1]


stack = Stack()
possible = True

for i in range(int(input())):
    n = int(input())

    while possible:
        if stack.max_value < n:
            stack.push(stack.max_value + 1)
        elif stack.is_empty():
            possible = False
        elif stack.top() == n:
            stack.pop()
            break
        elif stack.max_value > n:
            stack.pop()

print("\n".join(stack.history) if possible else "NO")
