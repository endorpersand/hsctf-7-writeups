# Emojis
## Problem
Esolang reversing!  
[Emojis.txt](./Emojis.txt)  

Author: JC01010

## Solution
Emojis utilizes an esolang (an [esoteric programming language](https://en.wikipedia.org/wiki/Esoteric_programming_language)), found [here](https://esolangs.org/wiki/Emoji-gramming).

To do this problem, I converted each command in the text to its respective line in Python ([emojic.py](./emojic.py)). Then, I took the output string and reversed it through the script to get the flag... aaaand the program was marked as having errors. I ended up getting something like `tr3v0r-pAck§p`.

Flag: `flag{tr3v0r_pAck3r}`