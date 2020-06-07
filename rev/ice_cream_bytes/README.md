# Ice Cream Bytes
## Problem
Introducing the new Ice Cream Bytes machine! Here’s a free trial: [IceCreamBytes.java](./IceCreamBytes.java)  
Oh, and make sure to read the user manual: [IceCreamManual.txt](./IceCreamManual.txt)

Author: wooshi
## Solution
As with most of the Reverse Engineering problems, the code simply takes your input, runs it through some functions, and checks it against a checkstring.

Here, it takes your string, plugs it in through `strawberryShuffle`, then `vanillaShuffle`, then `chocolateShuffle`, then `toppings` before checking it against a specified number of bytes from [IceCreamManual.txt](./IceCreamManual.txt).

So really, this problem is like most of the other Reverse Engineering problems, running the inverse of each function backwards on the checkstring, except you just need to include an additional step of finding the checkstring bytes (which you can do by printing the bytes to stdout).

`strawberryShuffle` reverses the array of bytes.
`vanillaShuffle` increments a byte in an array if its index is divisible by 0, otherwise it decrements the byte.
`chocolateShuffle` moves each byte in an array two elements rightward (if index is divisible by 0) or leftward (if index is not divisible by 0).
`toppings` adds a specified amount to each element.

Flag: `flag{ic3_cr34m_byt3s_4r3_4m4z1n9_tr34ts}`