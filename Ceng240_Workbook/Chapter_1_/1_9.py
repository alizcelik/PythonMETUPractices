'''
We want to cover the floor of a room with tiles without leaving any gap. All tiles are squares and are of the same length.
Write a program that inputs a width and length (two integers) of the room and calculates the maximum possible (integer) length of a tile and prints it.

Hint: You can use the  gcd()
  function from the  math
  module.

Sample I/O:

Input:
24
8

Output:
8

Input:
1
12

Output:
1
'''
import math

width=int(input())
length=int(input())

gcd=math.gcd(width,length)
print(gcd)