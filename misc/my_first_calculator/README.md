# My First Calculator
## Problem
I'm really new to python. Please don't break my calculator!

`nc misc.hsctf.com 7001`

There is a `flag.txt` on the server.

[calculator.py](./calculator.py)  

Author: meow
## Solution
Reading the [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)), it can be seen that calculator.py runs on Python *2.7*. This is important as Python 2.7 is deprecated, so there should be no real reason to use Python 2.7 in a regular file unless there's something important in Python 2.7. This reason this problem uses Python 2.7 due to its `input` function. 

Unlike in Python 3 (thankfully), the `input` function in Python 2.7 first *evaluates* the user input as a Python expression. This means we can arbitrarily run any Python expression from the script's server.

Since we know there's a `flag.txt` on the server, we can ask Python to open the file and to read it in one expression like so: `open('./flag.txt', 'r').read()`. However, nothing shows up, because we didn't tell Python to print the expression to stdout.

We can't use `print` to do this, as Python 2.7 `print` is a statement, not a function. So instead, we can use `sys.stdout.write`, like so: `__import__('sys').stdout.write(open('./flag.txt', 'r').read())`,  
or another `input`, like so: `input(open('./flag.txt', 'r').read())`

Flag: `flag{please_use_python3}`
(Listen to the flag.)