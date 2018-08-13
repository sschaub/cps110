def fact(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n * fact(n - 1)

answer = fact(3)
print(answer)