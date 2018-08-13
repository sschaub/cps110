def boo(x):
    q = x * 2
    return q

def foo(a, b):
    c = boo(a + b)
    return c

def main():
    d = foo(2, 3)
    
main()