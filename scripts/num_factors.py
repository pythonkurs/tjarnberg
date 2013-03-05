""" Script for factoring a series of large numbers """
import sys
from numpy import unique
from collections import Counter

def factorize(n):
    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return factors
        r = n % p
        if r == 0:
            factors.append(p)
            n = n / p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            p += 2
        else:
            p += 1

def serial(m):
    factors = []
    for i in xrange(m):
        factors.append(factorize(i))

    return factors

def multiproc(m,nproc=8):
    from multiprocessing import Pool

    pool = Pool(processes=nproc)
    results = pool.map_async(factorize, range(m))
    factors = results.get()
    return factors

def ipythonMP(m):
    from IPython.parallel import Client

    cli = Client()
    dview = cli[:]
    lbview = cli.load_balanced_view()
    return dview.map_sync(factorize,range(m))

    
if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == 's':
        factors = serial(500000)
    elif sys.argv[1] == 'm':
        factors = multiproc(500000)
    elif sys.argv[1] == 'i':
        factors = ipythonMP(500000)

    uniks = []
    for factor in factors:
        if factor != []:
            uniks.append(len(unique(factor)))

    c = Counter(uniks)
    print c
