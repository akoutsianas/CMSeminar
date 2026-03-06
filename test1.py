import time

def eratosthenes(N):
    primes = [i for i in range(2, N+1)]
    finish = False
    p0 = 2
    while not finish:
        # print(f"p0: {p0}")
        # print(f"primes before: {primes}")
        primes = [i for i in primes if i <= p0 or i % p0 != 0]
        # print(f"primes after: {primes}")
        if primes[-1] == p0:
            finish = True
        else:
            p0 = [i for i in primes if i > p0][0]
            # print(f"New p0: {p0}")
    return primes


print('Enter your N:')
N = int(input())
# N = 10000
t0 = time.time()
print(f"t0: {t0}")
primes = eratosthenes(N)
t1 = time.time()
print(f"time for eratosthenes method: {t1 - t0}")
print(f"The primes are: {primes}")

