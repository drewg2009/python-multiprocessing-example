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
        print("Time to square 1000000 numbers with multiprocessing")
        print(end - start)

    start = time.time()
    for val in range(1, 1000000):
        f(val)
    end = time.time()
    print("Time to square 1000000 numbers with a for loop")
    print(end - start)
