# xkcd.com/2247 v2
## Problem
Why pick a weird hill to die on when you could pick a soft hill to lie on?

Note: this challenge has been revised with a new flag. It was previously taken down and all solves for that challenge have been rolled back.

The flag format will be flag{a_bunch_of_words_with_underscores}. The flag is hidden inside the plaintext, and does not include a flag{}.

[HillREVISED.txt](./HillREVISED.txt)

## Solution
Through the challenge description or [the comic](http://xkcd.com/2247), you're supposed to figure out this problem involves a [Hill cipher](https://en.wikipedia.org/wiki/Hill_cipher). 

Hill ciphers use matrix multiplication to encrypt and decrypt a message, with the formula `EM = C (mod 26)` (encryption matrix * message matrix = ciphertext matrix).  
*Note*: A matrix modulo 26 just means that each of the elements in the matrix are taken to the mod of 26.  

To decrypt, you would just use <code>M = E<sup>-1</sup>C</code> (mod 26).  
*Note*: In this case, <code>E<sup>-1</sup></code> here does not represent the inverse of `E`, but rather the modular multiplicative inverse of E, which is defined with: <code>EE<sup>-1</sup> = E<sup>-1</sup>E = I (mod m)</code>.  

There's probably better ways to calculate <code>E<sup>-1</sup></code>, but <code>inv(E) * det(E) * det(E)<sup>-1</sup> (mod 26)</code> is how I did it.
( `inv(E)` represents the actual inverse of `E`, `det(E)` the determinant of `E`, and <code>det(E)<sup>-1</sup></code> the modular multiplicative inverse of det(E). )

The encryption matrix and ciphertext matrix is found by taking the encryption string and ciphertext string, converting each letter A to Z to their corresponding number from 0 to 25. Then these number values are placed horizontally left-right, up-down in the encryption matrix or vertically up-down, left-right in the ciphertext matrix. 
After finding the modular multiplicative inverse of `E`, multiplying by `C` to get back `M` and converting `M` back to a string, the flag can be found as a long string of words in a long piece of random text.

[Code](./matinv.py)  
Flag: `flag{imaginegivingtheplaintextandnottheciphertextriplmao}`
