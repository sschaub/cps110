def countdown(n: int):
    if n == 0:
        print("Boom!") # base case
    else:
        # recursive case
        print(n, "...")
        countdown(n - 1) # self call

    print('Finishing call to countdown; n = ', n)

countdown(3)

