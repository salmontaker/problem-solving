while True:
    s = input()
    stack = list()

    if s == ".":
        break

    for c in s:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(c)
                break
        elif c == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(c)
                break

    print("yes" if len(stack) == 0 else "no")
