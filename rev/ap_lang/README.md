# AP Lab: English Language
## Problem
The AP English Language activity will ask you to reverse a program about manipulating strings and arrays. Again, an output will be given where you have to reconstruct an input.  
[EnglishLanguage.java](./EnglishLanguage.java)  

Author: AC
## Solution
As with most of the Reverse Engineering problems, the code simply takes your input, runs it through some functions, and checks it against a checkstring.

Firstly, it is plugged into `transpose`, which takes a char at one index of the string and moves it to another specifically defined index.
Secondly, it is plugged into `xor`, which XORs specifically defined values to the ASCII codes of each char of the string.
Then, it does this two more times.

Simply run inverses of `xor` (`xor`'s inverse is itself) and `transpose` (see below) 3x on the checkstring to get back the desired input string.

Creating an inverse transpose in Python:
```py
transpose = [11,18,15,19,8,17,5,2,12,6,21,0,22,7,13,14,4,16,20,1,3,10,9]
flipped_transpose = [*range(len(transpose))]
flipped_transpose.sort(key=lambda x: transpose[x])

def inv_transpose(s):
    return ''.join( s[inverse_transpose[int(i)]] for i in range(len(s)) )
```

Flag: `flag{n0t_t00_b4d_r1ght}`