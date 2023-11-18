'''
In order to decide about the parity of a number (whether it is odd or even) it is enough to inspect its last digit.
Write a program that reads a three-digit number from the user.
Then checks if the number and reversed form of that number is even or odd (If the number is 123, then the reversed form is 321.)
If both are even, print “Even” or if both are odd print “Odd”.
If they are different from each other, then print their parity repectively (i.e. if the number is even print “Even Odd” else print “Odd Even”).

Hint: To find whether the reversed version is even or odd, inspecting only the first digit of the actual number is enough.

Sample I/O:

Input:
123

Output:
Odd

Input:
252

Output:
Even

Input:
324

Output:
Even Odd

Input:
857

Output:
Odd Even
'''

num = int(input())
x = str(num)[0]

if num % 2 == 0:
    if int(x) % 2 == 0:
        print('Even')
    else:
        print('Even Odd')
else:
    if int(x) % 2 != 0:
        print('Odd')
    else:
        print('Odd Even')


