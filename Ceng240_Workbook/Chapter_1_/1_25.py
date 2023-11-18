'''
1.25. Lego 5
You and your cousin are playing with Lego. Your cousin has built a line of blocks and you are roleplaying as the villain by controlling the action figure. You as the villain are going to destroy all the blocks between two given indices, so that block height at that index of the line will be 0. For your little cousin counting starts at 1 (not 0), so you act in conformity: you start counting with 1.

Can you find the final state of the Lego?

Hint: lego[0:5] = [1] replaces first 5 elements of an array with only one element as ‘1’. Use repetition operator for the list to solve this problem.

Sample I/O:

Input:
[1, 2, 3, 4, 5, 6]
1
3

Output:
[0, 0, 0, 4, 5, 6]

Input:
[2, 2, 7, 4, 9, 6, 1, 9, 2]
3
7

Output:
[2, 2, 0, 0, 0, 0, 0, 9, 2]
'''
lego_list = eval(input())
first_index = int(input()) - 1
last_index = int(input())

rep_list = lego_list[first_index:last_index] = [0] * (last_index - first_index)
new_list = list()
new_list.extend(lego_list[0:first_index])
new_list.extend(rep_list)
new_list.extend(lego_list[last_index:len(lego_list)])
print(new_list)
