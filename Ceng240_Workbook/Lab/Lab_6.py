'''
In this lab, you are asked to implement a function called find_extremities. The function definition is as follows:

find_extremities(big_list, mode)

big_list: A list containing lists of strings that represents integers, e.g. [lst1, lst2, ...] and lst1 = ["10", "85", ...].
mode: A string. Either "max" or "min".
The function should return a list containing:

A list (say return_list) that either contains maximum or minimum (as specified by the mode argument) element as integers from each list (lst1, lst2, ...) inside big_list.
A float that is the average of the integers in the return_list that you should return.
Notes:

Mode argument ("max" or "min") determines whether you should select maximum or minimum values from each list.
There will be at least one list inside of big_list and that list will have at least 1 element (i.e. no argument such as [[]]).
Warnings:

Your function should receive its data via its parameters only. Your submitted solution must NOT use any input() function.
Your function should return its results. Your submitted solution must NOT print anything.
Any return value that doesn't conform to the expected output type will be graded as zero.
The order of integers in the return_list does not matter as long as all the (necessary) integers are included in the list.
When using the emulator given with the link at the bottom, due to a small problem the result of a division can be shown as integer instead of a float (this happens only when the remainder is 0, e.g. 6/2.0 is shown as 3 instead of 3.0 still numerically correct) but this wont affect your grades since it is only a visual problem in emulator. Make sure that you use correct data types when performing the arithmetic operations and your result will be correct.
Hint:

You can "go over" big_list and find the max/min element of each list (according to the mode).
You can create an empty list to keep max/min values and update this list while going over big_list.
Example I/O


>>> find_extremities([["1","2","3","4"]], "max")
[[4], 4.0]
>>> find_extremities([["1", "6", "15", "4", "3"], ["11", "13", "0", "-5"]], "max")
[[15, 13], 14.0]
>>> find_extremities([["1", "6", "7", "4", "3"], ["11", "13", "0", "-5" ], ["-7", "-11"]], "min")
[[1, -5, -11], -5.0]
'''


def get_min_values(num_list):
    min_num = int(999999999)
    min_list = list()
    for i in range(len(num_list)):
        if isinstance(num_list[i], list):
            min_num = int(999999)
            for j in range(len(num_list[i])):
                if int(num_list[i][j]) < min_num:
                    min_num = int(num_list[i][j])
            min_list.append(min_num)
        else:
            if int(num_list[i]) < min_num:
                min_num = int(num_list[i])
    if not isinstance(num_list[0], list):
        min_list.append(min_num)

    return min_list


def get_max_values(num_list):
    max_num = int(-99999)
    max_list = list()
    for i in range(len(num_list)):
        if isinstance(num_list[i], list):
            max_num = int(-99999)
            for j in range(len(num_list[i])):
                if int(num_list[i][j]) > max_num:
                    max_num = int(num_list[i][j])
            max_list.append(max_num)
        else:
            if int(num_list[i]) > max_num:
                max_num = int(num_list[i])
    if not isinstance(num_list[0], list):
        max_list.append(max_num)

    return max_list


def get_average(num_list):
    total = sum(num_list)
    return total / len(num_list)


def find_extremities(big_list, mode):
    return_list = list()
    mode_list = list()
    if mode == "min":
        mode_list = (get_min_values(big_list))
    elif mode == "max":
        mode_list = (get_max_values(big_list))

    return_list.append(mode_list)
    return_list.append(get_average(mode_list))
    return return_list
