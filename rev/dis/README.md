# dis
## Problem
I lost my source code and all I can find is this disassembly.  
[disas](./disas)  

Author: hmmm
## Solution
Opening the disas file shows some bytecode, specifically Python bytecode (as evidenced by mentions of `listcomp` and `vuln.py`). As mentioned in the challenge description, the goal is to convert this into readable Python code.

Python has good documentation explaining what each of the instructions mean [here](https://docs.python.org/3/library/dis.html?highlight=dis#bytecode-analysis).  
*Note*: `python3 -m dis file.py` prints disassembled Python bytecode to stdout.

Though honestly, even with this documentation, it still was very confusing what things mean. For instance, what does `LOAD_FAST` mean?

To figure this out, I just incrementally went through the functions and *guessed* what I thought they meant, checking to confirm with `python3 -m dis file.py`.

Eventually, I ended up with something like:
```py
def a(s):
    o = [0] * len(s)

    for i, c in enumerate(s):
        o[i] = c * 2 - 60
    return o

def b(s, t):
    for x, y in zip(s, t):
        yield x + y - 50

def c(s):
    return [c + 5 for c in s]

def e(s):
    s = [ord(c) for c in s]
    o = [(c ^ 5) - 30 for c in b(a(s), c(s))]
    return bytes(o)

def main():
    s = input('Guess?')
    o = b'\xae\xc0\xa1\xab\xef\x15\xd8\xca\x18\xc6\xab\x17\x93\xa8\x11\xd7\x18\x15\xd7\x17\xbd\x9a\xc0\xe9\x93\x11\xa7\x04\xa1\x1c\x1c\xed'
    if e(s) == o:
        print('Correct!')
    else:
        print('Wrong...')
```
This is quite confusing still, but in reality, `e` and the functions that create `e` make it look more complicated than it seems.  

`a(s)` can be simplified to `[c * 2 - 60 for c in s]`  
`b(s, t)` creates a list by adding the two elements with matching indexes across the two lists and subtracting 50 from that number.  

All in all, `e(s)` simplifies to `lambda s: bytes( (c * 3 - 105) ^ 5 - 30 for c in s )`.  
This function can be reversed very easily (`lambda bt: ''.join([chr( (((b + 30) ^ 5) + 105) // 3 ) for b in bt])`), allowing us to get the flag using the checkstring.  

Flag: `flag{5tr4ng3_d1s45s3mbly_1c0a88}`