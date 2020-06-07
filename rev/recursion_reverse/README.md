# Recursion Reverse
## Problem
Jimmy needs some help figuring out how computers process text, help him out!  
[AscII.java](./AscII.java)  

Author: AD
## Solution
As with most of the Reverse Engineering problems, the code simply takes your input, runs it through some functions, and checks it against a checkstring.

Firstly, each char's ASCII code increments by a value determined by `pickNum(index + 1)`, then is modded by 127.  
Then, the string is reversed.

So, just reverse the string again, subtract `pickNum(index + 1)` from each of the ASCII codes and mod by 127 again.  
*Note*: Java operator `%` returns negative if the dividend is negative. To prevent this, you can use `((x % y) + y) % y`.

Flag: `flag{AscII is key}`
