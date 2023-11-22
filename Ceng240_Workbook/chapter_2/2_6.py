'''
Imagine a garden of apple trees in the harvest time. Assuming the trees are planted in a regular way, in  M
  rows each of which has  N
  trees. Each tree has a different apple count. These count of apples can be represented as a matrix of  M×N
 . There are  M
  workers each responsible of collecting the apples in a horizontal row.

Write a script to find out the row which will procude the highest count of apple and print that row.

M
  and  N
  are two positive integers.

Assume that the matrix, namely the ‘list of lists of integers’, representing the apple counts will be given to you in a variable  G
 .

Sample I/O:

Input:
G = [[30, 40, 20, 50], [60, 20, 40, 10], [50, 30, 70, 60], [30, 40, 40, 20]]

Output:
[50, 30, 70, 60]

Input:
G = [[20, 10, 20, 30, 80, 80, 50, 80, 40, 40], [20, 10, 50, 10, 20, 90, 90, 20, 60, 20],
     [50, 50, 90, 10, 60, 30, 60, 20, 40, 60], [20, 80, 60, 80, 90, 20, 20, 60, 80, 30],
     [10, 30, 50, 60, 20, 10, 90, 50, 80, 70]]

Output:
[20, 80, 60, 80, 90, 20, 20, 60, 80, 30]
'''

apples = eval(input()[4:])
max_sum_apple = 0
max_row_index = 0

for row in range(len(apples)):
    row_sum = 0
    for col in range(len(apples[row])):
        row_sum += apples[row][col]
    if row_sum > max_sum_apple:
        max_sum_apple = row_sum
        max_row_index = row
print(apples[max_row_index])



