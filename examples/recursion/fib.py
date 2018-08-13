def fib(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

result = fib(6)
print(result)