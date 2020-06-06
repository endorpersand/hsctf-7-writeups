import re

with open('./info.txt', 'r') as f:
    ws = f.read().splitlines()

def diagonals(L):
    """
    https://stackoverflow.com/a/31373955/190597 (unutbu)
    >>> L = array([[ 0,  1,  2],
                   [ 3,  4,  5],
                   [ 6,  7,  8],
                   [ 9, 10, 11]])

    >>> diagonals(L)
    [[9], [6, 10], [3, 7, 11], [0, 4, 8], [1, 5], [2]]
    """
    h, w = len(L), len(L[0])
    return [[L[h - p + q - 1][q]
             for q in range(max(p-h+1, 0), min(p+1, w))]
            for p in range(h + w - 1)]


def antidiagonals(L):
    """
    >>> L = array([[ 0,  1,  2],
                   [ 3,  4,  5],
                   [ 6,  7,  8],
                   [ 9, 10, 11]])

    >>> antidiagonals(L)
    [[0], [3, 1], [6, 4, 2], [9, 7, 5], [10, 8], [11]]
    """
    h, w = len(L), len(L[0])
    return [[L[p - q][q]
             for q in range(max(p-h+1,0), min(p+1, w))]
            for p in range(h + w - 1)]

diags = [''.join(d) for d in diagonals(ws)] + [''.join(d) for d in antidiagonals(ws)]


check = ''.join([f'{ord(c):b}'.rjust(8, '0') for c in "flag"]) # flag in binary forwards
check2 = ''.join(reversed(check)) # flag in binary backwards

l = [] # list with flag
i = None # index of flag in list

# check rows
if any(check in row for row in ws):  
    l = next(row for row in ws if check in row)
    i = l.index(check)

if any(check2 in row for row in ws): 
    l = next(row for row in ws if check2 in row)
    i = l.index(check2)

# check cols
if any(check in col for col in zip(*ws)):  
    l = next(col for col in zip(*ws) if check in col)
    i = l.index(check)

if any(check2 in col for col in zip(*ws)): 
    l = next(col for col in zip(*ws) if check2 in col)
    i = l.index(check2)

# check diags
if any(check in diag for diag in diags):  
    l = next(diag for diag in diags if check in diag)
    i = l.index(check)

if any(check2 in diag for diag in diags): 
    l = next(diag for diag in diags if check2 in diag)
    i = l.index(check2)

s = l[i:]
# convert binary to ascii starting from the start of flag{...}
print( *(chr(int(x, 2)) for x in re.findall('.' * 8, s)) )