# Apple Pie
## Problem
My friend gave this *program* to me, but I'm not sure what it means.

Note: Your output will have to be parsed into decimal representations of ASCII characters.

[ApplePie_1.pie](./ApplePie_1.pie)  

Author: AC
## Solution
Apple Pie utilizes an esolang (an [esoteric programming language](https://en.wikipedia.org/wiki/Esoteric_programming_language)), found [here](https://esolangs.org/wiki/Apple_Pie).

To do this problem, I converted each command to Python ([pie.py](./pie.py)) and ran the code, which returned `051112116119048110052`. Every triplet represents an ASCII character, so just take each triplet, convert to integers, and get the respective ASCII character. ~~Disregard the fact that I spent 1-2 days realizing that JS interprets `051` as octal representation before getting the flag.~~

Flag: `flag{3ptw0n4}`