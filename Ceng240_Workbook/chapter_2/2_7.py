'''
2.7. Exercise: New Apple Garden Tree 2
Imagine the same garden in the question above. This time, the workers decide to divide the garden vertically. Namely, each worker will be responsible for the trees in a column.
Write a script to find out which column produces the maximum number of apples in a given garden and print it.
Hint: You need to adjust the nested loop in the previous solution, so that the traverse of the garden can be column-wise.
Sample I/O:

Input:
G = [[30, 40, 20, 50], [60, 20, 40, 10], [50, 30, 70, 60], [30, 40, 40, 20]]

Output:
[30, 60, 50, 30]

Input:
G = [[90, 10, 90, 40, 10], [70, 70, 80, 20, 30], [40, 60, 20, 90, 40], [40, 50, 50, 30, 20], [20, 30, 30, 80, 30], [90, 70, 20, 10, 60], [70, 90, 40, 40, 10]]

Output:
[90, 70, 40, 40, 20, 90, 70]
'''

apples = eval(input()[4:])

max_col_sum = 0
max_col = 0

for col in range(len(apples[0])):
    row_sum = 0
    for row in range(len(apples)):
        row_sum += apples[row][col]
    if row_sum > max_col_sum:
        max_col_sum = row_sum
        max_col = col
result = list()
for row in range(len(apples)):
    result.append(apples[row][max_col])
print(result)