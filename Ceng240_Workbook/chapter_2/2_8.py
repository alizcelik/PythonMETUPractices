'''
In this question it is asked to determine whether the first half of a string is exactly the same of its second half. If the string is not halvable (i.e. has odd number of elements) then and error message has to be printed.

For example, “abab” is such a string. When it is divided into two equal parts, the parts are “ab” and “ab” and these are the same. On the other hand, “abba” is not such a string, because the two halves are “ab” and “ba” and they are not the same. If the input string is such a ‘repeated string’, you should print “Yes”, otherwise, you should print “No”. If the length of the string is odd then print “Error”.
Sample I/O:

Input:
abaaba

Output:
Yes

Input:
abbbba

Output:
No

Input:
a

Output:
Error

Input:
aba

Output:
Error
'''

text = input()
half = len(text) / 2

if half % 1 == 0:
    if text[:int(half)] == text[int(half):]:
        print("Yes")
    else:
        print("No")
else:
    print("Error")