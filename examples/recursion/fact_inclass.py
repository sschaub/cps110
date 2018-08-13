def fact(n: int) -> int:
    print("Processing n = ", n)
    if n == 0:
        return 1
    elif n > 0:
        return n * fact(n-1)
    else:
        raise Exception('Cannot process negative n')

x = fact(3)
print(x)