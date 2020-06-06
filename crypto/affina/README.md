# Affina and the Quadratics
## Problem
Affina was struggling with her graphing quadratics homework. Bored, she decided to cheat by using Desmos to graph the given quadratic, and then realized that she could use it to send messages to her best friend without anyone noticing!

Note: Affina uses a 26 character charset and the numbers are encoded differently.

Affina_and_the_Quadratics.txt:
```
Affina was struggling with her graphing quadratics homework. Bored, she decided to cheat by using Desmos to graph the given quadratic, and then realized that she could use it to send messages to her best friend without anyone noticing!

She sent the following message to her friend: 7rr4p6_4e_4ph6bo8hap2?

Can you decrypt it using the image of the quadratic Affina used? Note: the flag should make relative sense.
```

![Quadratic](./images/affffinaaaa-page-001.jpg)

Author: Plate_of_Sunshine
## Solution
By the name Affina, this problem is about [affine ciphers](https://en.wikipedia.org/wiki/Affine_cipher).  
In an affine cipher, each letter is mapped to a number from 0 to 25 based off its position in the alphabet. Each value is plugged into the function `f(x) = ax + b (mod 26)` for some defined a and b.  
In the provided picture of the graph describes the function y = <code>x<sup>2</sup> + 3x + 2</code>. From the picture, you're supposed to get that `a = 3`, `b = 2`. 

After running the ciphertext through some online decryptor, you get `7ff4n6_4s_4nt6re8tin2`.
You are supposed to figure out that the numbers Caesar shift backwards by 3. You can do this by realizing it's trying to spell out `4ff1n3_1s_1nt3re5tin9` ("affine is interesting").

Flag: `flag{4ff1n3_1s_1nt3re5tin9}`