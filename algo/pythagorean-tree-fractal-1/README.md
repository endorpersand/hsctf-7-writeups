## Pythagorean Tree Fractal 1
# Problem
![Pythagorean Tree Fractal 1](./images/Pythagorean_Tree_Fractal.png)
Author: Plate_of_Sunshine

# Solution
The amount of squares added in each stage double from the last stage. The sum of the number of squares here can be written with the formula:  
1 + 2 + 4 + 8 + 16 + … + 2<sup>n</sup> - 1 = 2<sup>n</sup> - 1  
Since n = 50, the solution is 2<sup>50</sup> - 1.

Flag: `flag{1125899906842623}`
