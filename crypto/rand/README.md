# Randomization 1 & 2
## Problem
### Randomization 1
Hear ye, for I have constructed another diversionary exercise taking the form of a competition whose contents consist of the repeated divination of an arbitarily and pseudorandomly generated numeric!

Connect with nc crypto.hsctf.com 6001.

### Randomization 2
I was tired of writing verbose descriptions so I went and drank some coffee. Now I'm coding in Java. Darn it.

The C implementation implements the PRNG used in java.util.Random, but outputs all 64 bits instead of the top 32.

Connect with nc crypto.hsctf.com 6002.

Author: PMP
## Solution
Randomization 1 & 2 both use an [LCG](https://en.wikipedia.org/wiki/Linear_congruential_generator) to generate the next value in the "randomized" sequence.  
From the Wikipedia article, an LCG can be described with the recurrence relation <code>X<sub>n + 1</sub> = a * X<sub>n</sub> + b</code>.

The multiplier, increment, and modulus for the LCG can be found in the disassembled ELF binary.
