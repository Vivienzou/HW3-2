HW3-1
=====
%time
def f(p,m):
    p = 0
    for i in range(10001):
        m = i**2 
        p = m + p


%time
cython("""
def f(p,m):
    p = 0
    for i in range(10001):
        m = i**2 
        p = m + p""")

