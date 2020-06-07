# AP Lab: Statistics
## Problem
In AP Statistics, you will be shown a program consisting of manipulated and random numbers. Similarly to AP 3D Design, only a compiled .class file will be given rather than Java code.

Note: In the program given, "guess" will need to be in flag format, flag{...}, for the program to accept "guess" as the flag.

[APStatistics.java (decompiled)](APStatistics.java)

Author: AT
## Solution
As with most of the Reverse Engineering problems, the code simply takes your input, runs it through some functions, and checks it against a checkstring.
The difference this time is that one of the functions `toNumbers` uses `Math.random()`, meaning the program is not deterministic, and as well, a function used, `swapArray`, is not injective, and as such, there is not one definitive inverse for an output of `swapArray`.

Something to notice about `toNumbers` is that `Math.random()` must return 5. Otherwise, no input to the program will ever return true.

To realize this, we can analyze what happens to `flag{` when we plug it into the program.
The characters' ASCII codes are changed, and then they get `swapArray`ed twice.

The ASCII codes of `flag{`: `[102, 108, 97, 103, 123]` have to change and scramble in such a way such that the first three values equal the first three values of the ASCII code array of the checkstring.  
Under `Math.random()` = 5, `flag{` becomes `[113, 116, 113, 110, 102]`, which matches the first three values of the checkstring.

Why three? Well, `swapArray` basically acts as one iteration of bubble sort. In one iteration of bubblesort, the smallest value is moved to the end. But while this is being done, values larger than the contender for smallest value do not move place in the array relative to the other elements, only the smallest value seen so far in the array. As we're doing `swapArray` twice, the two smallest values move places, but everything else stays in place. So the three values that were already on the left of the array stay there, because they didn't move, only the two smallest values moved. Did that make sense? I dunno.

After finding out `Math.random()` must return 5... basically I just guessed and checked until I got somewhere. Firstly, I moved around the ASCII code array of the checkstring until `swap_array(swap_array(x)) == check_string_list` With Python (after porting the code to Python). Then, after x is found, you can reverse it through an inverse of `toNumbers` to find the flag. Keep in mind though, that the flag must be *readable*, and unreadable flags may show up. If this occurs you just need to manipulate the list more.

Flag: `flag{tenpercentofallstatisticsarefake}`