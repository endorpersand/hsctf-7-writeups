# Smol E
## Problem
Anshul has a message that he wants to send to Disha using RSA. He padded the message with a random padding and sent it to Disha, but she didn’t receive the message. However, she was able to receive the message after a second attempt from Anshul. You were able to intercept both of Anshul’s ciphertexts, and you are also given Anshul’s RSA public key. Can you recover the message?

SmolE.txt
```
N = 163741039289512913448211316444208415089696281156598707546239939060930005300801050041110593445808590019811244791595198691653105173667082682192119631702680644123546329907362913533410257711393278981293987091294252121612050351292239086354120710656815218407878832422193841935690159084860401941224426397820742950923

E = 3

C1 = 110524539798470366613834133888472781069399552085868942087632499354651575111511036068021885688092481936060366815322764760005015342876190750877958695168393505027738910101191528175868547818851667359542590042073677436170569507102025782872063324950368166532649021589734367946954269468844281238141036170008727208883

C2 = 42406837735093367941682857892181550522346220427504754988544140886997339709785380303682471368168102002682892652577294324286913907635616629790484019421641636805493203989143298536257296680179745122126655008200829607192191208919525797616523271426092158734972067387818678258432674493723618035248340048171787246777
```

Author: AC
## Solution
As the title entails, you should look for an exploit related to small `E`'s, specifically `E = 3`. One such instance of this is [Coppersmith's short-pad attack](https://en.wikipedia.org/wiki/Coppersmith's_attack#Coppersmith’s_short-pad_attack), an application of [Coppersmith's theorem](https://en.wikipedia.org/wiki/Coppersmith's_attack).  
Reading through the section on the short-pad attack on Wikipedia, we can see it is used when two identical messages have been poorly padded before being encrypted, perfectly fitting the scenario.

Instead of spending the brain power to try to figure out what the heck this attack is and how to program it, you can use [someone else's brain power](https://github.com/pwang00/Cryptographic-Attacks/blob/master/Public Key/RSA/coppersmith_short_pad.sage). This can be copied into SageMath (math system built on top of Python)'s [code evaluator](https://sagecell.sagemath.org/).

When done, this returns something similar to `1426051161596273413795556654328320105145439332147585418507576775870780450590379567453641429082640842935901398525237698534587016076610446383728128936582478631369081375319103785503713430762835018940932512662482247881629813321166872870577809910090459052486979919351413039719867069160`.  

This cannot be converted into ASCII at this stage, though. If you try, you get a bunch of gibberish.  
In Coppersmith's short-pad attack, the number of bits in padding, `m`, is defined as `n // e2` bits (n = num of bits in the public modulus, e = public encryption exponent).  
So, this padding needs to be removed (via `large_num >> m`), and then finally the number can be converted to ASCII.

Flag: `flag{n0t_4_v3ry_sm0l_fl4g}`
