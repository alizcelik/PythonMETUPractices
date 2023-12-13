'''
You are to implement a function that processes a list of transactions. The function definition and its parameters are as follows:

process_transactions(transactions, lower_bound, upper_bound)
-transactions: A list of floats.
-lower_bound: A float.
-upper_bound: A float.

The function should return a list of three items:
- The first item is a list containing the transactions lower than or equal to the lower_bound.
- The second item is a list containing the transactions between lower_bound and upper_bound.
- The third item is a list containing the transactions greater than or equal to the upper_bound.

Notes:
- Your function should receive its data via its parameters only. Your submitted solution must NOT use any input() function.
- Your function should return its results. Your submitted solution must NOT print anything.
- Any return value that doesn't conform to the expected output type will be graded as zero.

Hint:
- Create separate empty lists for the three items and fill them up accordingly.

Example I/O:

#>>> process_transactions([27.5, 34.0, 73.3, 31.0, 66.0], 30.0, 40.0)
[[27.5], [34.0, 31.0], [73.3, 66.0]]

#>>> process_transactions([27.89, 34.44, 32.21, 31.26, 66.71], 20.0, 34.44)
[[], [27.89, 32.21, 31.26], [34.44, 66.71]]

'''

def process_transactions(transactions, lower_bound, upper_bound):

    lower_list = list()
    upper_list = list()
    mid_list = list()
    combo_list = list()

    for transaction in transactions:
        if transaction <= lower_bound:
            lower_list.append(transaction)
        elif transaction >= upper_bound:
            upper_list.append(transaction)
        else:
            mid_list.append(transaction)

    combo_list.append(lower_list)
    combo_list.append(mid_list)
    combo_list.append(upper_list)
    return combo_list

print(str(process_transactions([27.5, 34.0, 73.3, 31.0, 66.0], 30.0, 40.0)) == '[[27.5], [34.0, 31.0], [73.3, 66.0]]')
print(str(process_transactions([27.89, 34.44, 32.21, 31.26, 66.71], 20.0, 34.44)) == '[[], [27.89, 32.21, 31.26], [34.44, 66.71]]')


