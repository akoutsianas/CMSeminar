import time

def fibonacci(n):
    if (n == 1) or (n == 2):
        return 1
    fn = 1
    fn1 = 1
    for i in range(n-2):
        temp = fn
        fn = fn + fn1
        fn1 = temp
    return fn

N = 5000
for n in range(1, N+1):
    # print(f"n={n}")
    t0 = time.time()
    Fn = fibonacci(n)
    t1 = time.time()
    print(f"F{n}: {Fn} with time: {t1- t0}, n={n}")