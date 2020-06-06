# AP Lab: Computer Science Principles
## Problem
This activity will ask you to reverse a basic program and solve an introductory reversing challenge. You will be given an output that is to be used in order to reconstruct the input, which is the flag.  
[ComputerSciencePrinciples.java](./ComputerSciencePrinciples.java)  

Author: AC
## Solution
As with most of the Reverse Engineering problems, the code simply takes your input, runs it through some functions, and checks it against a checkstring.

Firstly, it's plugged through `shift`, which decreases the ASCII code of each char by the index of the char in the string.
Secondly, it's plugged through `shift2`, which increases the ASCII code of each char by the number of digits in the ASCII code.

Simply create inverses of `shift` and `shift2`, and run the checkstring in reverse, to get the flag.

Flag: `flag{intr0_t0_r3v}`