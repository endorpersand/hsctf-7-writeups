# Unexpected
## Problem
Alice, Bob, and Carol are really close friends; in fact, they are so close, they even share the same primes in their RSA public keys! Alice has N = PQ, Bob has N = QR, and Carol has N = PR, where P,Q,R are 1024 bit primes. All three also use the same public exponent e = 65537. Can you recover the three plaintexts?

[Unexpected.txt](./Unexpected.txt)

Author: AC
## Solution
To decrypt RSA, you need the primes involved in creating the public and private keys. This is very easy to do in this problem because:
 * Since we know `N1 = P * Q`, `N2 = Q * R`, `N3 = P * R`, we also know <code>N1 * N2 * N3 = P<sup>2</sup> * Q<sup>2</sup> * R<sup>2</sup></code>.
 * Take the [square root of this large integer](https://stackoverflow.com/questions/15390807/integer-square-root-in-python) to get `P * Q * R`.
 * Now by dividing `P * Q * R` by `N1`, `N2`, or `N3`, we can easily get `R`, `P`, and `Q`.
 * From here, it is pretty much [regular RSA decryption](https://simple.wikipedia.org/wiki/RSA_algorithm#Operation).

*Note*: For RSA problems, you will usually get a number. You need to convert this number into a hex string, split the string every two characters, and find the respective character of the hex ASCII code to get the flag.

[Haphazardly Made Code](./code.py)  
Flag: `flag{n0_0n3_3xp3ct5_th3_sp4nish_inquisiti0n!}`