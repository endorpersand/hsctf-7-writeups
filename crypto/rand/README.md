# Randomization 1 & 2
## Problem
### Randomization 1
Hear ye, for I have constructed another diversionary exercise taking the form of a competition whose contents consist of the repeated divination of an arbitarily and pseudorandomly generated numeric!

Connect with `nc crypto.hsctf.com 6001`.

### Randomization 2
I was tired of writing verbose descriptions so I went and drank some coffee. Now I'm coding in Java. Darn it.

The C implementation implements the PRNG used in java.util.Random, but outputs all 64 bits instead of the top 32.

Connect with `nc crypto.hsctf.com 6002`.

Author: PMP
## Solution
Randomization 1 & 2 both use an [LCG](https://en.wikipedia.org/wiki/Linear_congruential_generator) to generate the next value in the "randomized" sequence.  
From the Wikipedia article, an LCG can be described with the recurrence relation <code>X<sub>n + 1</sub> = a * X<sub>n</sub> + b</code>.

The multiplier, increment, and modulus for the LCG can be found in the disassembled ELF binary. In a UNIX terminal, `objdump -d file` disassembles the ELF binary.  
By scanning through the disassembled code, you can figure out that the function controlling the LCG is the function `next`.
### Rand 1
```
next:
    125d:	55 	pushq	%rbp
    125e:	48 89 e5 	movq	%rsp, %rbp
    1261:	b8 25 00 00 00 	movl	$37, %eax
    1266:	0f b6 15 b3 2d 00 00 	movzbl	11699(%rip), %edx
    126d:	0f af c2 	imull	%edx, %eax
    1270:	83 c0 41 	addl	$65, %eax
    1273:	88 05 a7 2d 00 00 	movb	%al, 11687(%rip)
    1279:	0f b6 05 a0 2d 00 00 	movzbl	11680(%rip), %eax
    1280:	0f b6 c0 	movzbl	%al, %eax
    1283:	5d 	popq	%rbp
    1284:	c3 	retq
```
In AT&T syntax, the -b, -w, -l, -q after an instruction represents the type of number of the argument (8-bit, 16-bit, 32-bit, 64-bit).
[Here](https://www.cs.yale.edu/flint/cs421/papers/x86-asm/asm.html)'s more info on x86 Assembly. 

Differences in x86-64 Assembly:
 * 64-bit registers exist, and they start `%r`, replacing the `%e` of 32-bit registers.
 * Like how a 16-bit register is the lower 16 bits of its corresponding 32-bit register (e.g. %ax and %eax), a 32-bit register is the lower 32 bits of its corresponding 64-bit register (e.g. `%eax` and `%rax`).
Also `movz` means to zero-out a register and then move the bits over.

Here, this code approximately translates to:
 * Move `37` (dec) to `%eax`.
 * Move arg of function to `%edx`.
 * Integer multiply `%eax` by `%edx` and set `%eax` to the result.
 * Add `65` to `%eax`.
 * Zero-out all but the lower 8 bits of `%eax`.
From this, the LCG recurrence relation is <code>37x + 65 (mod 2<sup>8</sup>)</code>. As they give us the previous value in the sequence, we can use the LCG to find the following values of the sequence.

### Rand 2
```
next:
    12b0:	55 	pushq	%rbp
    12b1:	48 89 e5 	movq	%rsp, %rbp
    12b4:	48 8b 05 ed 2d 00 00 	movq	11757(%rip), %rax
    12bb:	48 ba 6d e6 ec de 05 00 00 00 	movabsq	$25214903917, %rdx
    12c5:	48 0f af c2 	imulq	%rdx, %rax
    12c9:	ba 0b 00 00 00 	movl	$11, %edx
    12ce:	48 01 d0 	addq	%rdx, %rax
    12d1:	48 89 05 d0 2d 00 00 	movq	%rax, 11728(%rip)
    12d8:	48 8b 05 c9 2d 00 00 	movq	11721(%rip), %rax
    12df:	5d 	popq	%rbp
    12e0:	c3 	retq
```
Here, the LCG relation is <code>25214903917x + 11 (mod 2<sup>64</sup>)</code> (64 because of the limitation of the 64-bit register).
