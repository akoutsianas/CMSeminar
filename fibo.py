import time

def fibonacci(n):
    if (n == 1) or (n == 2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

N = 50
for n in range(1, N+1):
    # print(f"n={n}")
    t0 = time.time()
    Fn = fibonacci(n)
    t1 = time.time()
    print(f"Fn: {Fn} with time: {t1- t0}, n={n}")