def frq(s):
    dct = {}
    n = 0
    for c in s:
        if c in dct:
            dct[c] += 1
        else:
            dct[c] = 1
        n += 1
    for c in dct: dct[c] /= n
    return dct


def carre(x):
    return x * x

def harmonic(n):
    total = 0
    for k in range(1,n+1):
        total += 1/k
    return total