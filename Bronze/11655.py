for c in input():
    if c.islower():
        print(chr((ord(c) - ord("a") + 13) % 26 + ord("a")), end="")
    elif c.isupper():
        print(chr((ord(c) - ord("A") + 13) % 26 + ord("A")), end="")
    else:
        print(c, end="")
