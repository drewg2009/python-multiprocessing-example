from multiprocessing import Pool
import time
import os

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(None) as p:
        start = time.time()
        p.imap(f, range(1,1000000))
        end = time.time()
        print(end - start)

    start = time.time()
    for val in range(1, 1000000):
        f(val)
    end = time.time()
    print(end - start)
