import itertools


def primes():
    a = 1
    while True:
        a += 1
        k = 0
        for x in range(2, a+1):
            if k > 1:
                break
            if a%x == 0:
                k += 1
        if k == 1:
            yield a

print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]