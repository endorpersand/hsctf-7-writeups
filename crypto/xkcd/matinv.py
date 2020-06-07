from fractions import Fraction
from copy import deepcopy
import re

with open('encrypt.txt', 'r') as f:
    emat = re.findall(r'.' * 100, f.read())
    emat = [[ord(char) - ord('a') for char in row] for row in emat]

with open('ciphertext.txt', 'r') as f:
    cmat = re.findall(r'.' * 100, f.read())
    cmat = [[ord(char) - ord('a') for char in row] for row in zip(*cmat)]

mod = 26

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def invert(mat, mod: int = mod):
    '''
    Finds the modular multiplicative inverse of a matrix
    '''
    mat = deepcopy(mat)
    det = 1
    # ^ det of mat before invert
    # 
    # on conversion to reduced echelon form...
    # row-swap: 1 / det *= - 1
    # scaling row (and writing) to matrix: 1 / det *= scale
    # adding scaled row to another row: 1 / det stays same
    # 
    # (reg inv * det * det^-1) % mod = modular inverse
    # 

    def mut_row(i: int, scale: int = 1):
        '''
        Scales and modifies row mat[i], changes det
        '''
        nonlocal det
        if scale == 1: return
        row = mat[i]
        for j, elem in enumerate(row):
            row[j] = elem * scale
        det *= Fraction(1, scale)

    def immut_row(i: int, scale: int = 1) -> list:
        '''
        Copies row mat[i], scales it, and returns scaled row
        '''
        if scale == 1: return mat[i]
        return [elem * scale for elem in mat[i]]

    def swap_rows(i: int, j: int):
        '''
        Swap rows mat[i] and mat[j], and change det
        '''
        nonlocal det
        mat[i], mat[j] = mat[j], mat[i]
        det *= -1

    def add_row(i: int, r: list):
        '''
        Adds row r to mat[i].
        '''
        for j in range(len(r)):
            mat[i][j] += r[j]

    # add identity matrix to the right of matrix
    for i in range(len(mat)):
        iden_row = [0] * len(mat)
        iden_row[i] = 1
        mat[i] += iden_row

    for i in range(len(mat)):

        if mat[i][i] == 0:
            try:
                ni = next(j for j in range(len(mat)) if mat[j][i] != 0 and j > i)
            except StopIteration:
                raise ValueError('Matrix is not invertible.')
            swap_rows(i, ni)

        mut_row(i, Fraction(1, mat[i][i])) # mut_row(i, 1 / mat[i][i]) to assure mat[i][i] = 1

        for j in range(len(mat)):
            if i == j: continue
            add_row(j, immut_row(i, -mat[j][i]) )

    det = int(det)
    
    ## get rid of identity matrix on the left
    for i in range(len(mat)):
        mat[i] = mat[i][len(mat):]

    # reg inv * det to convert matrix to all ints
    for i in range(len(mat)):
        mat[i] = [int(elem * det) for elem in mat[i]]

    det_inv = modinv(det, mod)

    # multiply by det^-1 (mod mult inv of det) to cancel out the prev mult
    for i in range(len(mat)):
        mat[i] = [(elem * det_inv) % mod for elem in mat[i]]
    
    return mat

def dotmul(vec1: list, vec2: list) -> list: # does not mutate mats
    if len(vec1) != len(vec2): raise ValueError('Cannot dot multiply vectors of varying lengths.')
    return sum(a * b for a, b in zip(vec1, vec2))

def matmul(mat1, mat2, mod: int = mod): # does not mutate mats
    return [[dotmul(r, c) % mod for c in zip(*mat2)] for r in mat1]

emat_inv = invert(emat)

mmat = matmul(emat_inv, cmat) 
mmat = ''.join([ ''.join(chr(ordin + ord('a')) for ordin in row) for row in zip(*mmat) ])
with open('hill_msg.txt', 'w') as f:
    f.write(mmat)