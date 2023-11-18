'''
In this question you are required to write a program that prints the innermost m elements in list format for a given list of length n. It is guaranteed that m ≤ n, and both numbers m and n are of the same parity.

Sample I/O:

Input:
[1,2,3,4,5,6]
2

Output:
[3,4]


Input:
[10,4,6,2,7,32,6,76,99]
3

Output:
[2,7,32]
'''
number_list = eval(input())
innermost = int(input())

length = len(number_list)
first_index = int((length - innermost) / 2)
print(first_index)
last_index = first_index + innermost
print(last_index)

print(number_list[first_index:last_index])
