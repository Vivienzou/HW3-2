HW3-1
=====
def f(p,m):
    p = 0
    for i in range(10001):
        m = i**2 
        p = m + p

timeit("f")
