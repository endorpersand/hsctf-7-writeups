def printv(v):
    print(''.join(reversed(str(v))))  
def printc(c):
    print( chr(ord(c) -1) )
def tern(x):
    return range(int(x, 3))
def run():
    z = 0
    o = 1
    printv(z)
    t = 2
    l = 5 * 1
    printv(l)
    for i in tern('10'):
        printv(o)

    printv(t)
    for i in tern('02'):
        printv(o)
        
    w = l + 1
    printv(w)
    n = 13 * 70
    n = n + 1
    printv(n)
    printc('1')
    p = 0
    k = 0
    for i in tern('20'):
        p = p + 1
        k = k + 1

    for i in tern('22'):
        k = k + 1

    k = k * p
    printv(k)
    printc('2')
    printc('2')
    l = l - 5
    printv(l)
    printv(l)
    a = 1
    t = 1
    for i in tern('11'):
        p = 2 * a
        p = p + 1
        t = t + p
        a = a + 1

    printv(t)

run()