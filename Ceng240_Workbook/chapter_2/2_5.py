'''
In a 2D board ( N×N
 ) game played by two teams (red and blue), teams select cells in turns, and each cell gives some random points to team player in it. After the game is over, the result is given in a matrix where the negative and positive values indicate the cells are occupied by the red and the blue team respectively.
Write a program which outputs the points gathered by the red team.
N
  can be any positive number that is greater than or equal to 3.

It is guaranteed that every cell in the board has positive or negative value at the end of the game (i.e. no zero value).

Assume that the list of lists of integers representing the resulting board will be given to you as the variable  B
 .

Sample I/O:

Input:
B = [[3, 4, 4], [2, -5, -2], [-4, 2, -4]]

Output:
15

Input:
B = [[-3, -2, -1, -4], [4, -2, 4, 5], [-2, -1, -2, 5], [3, 1, 4, -1]]

Output:
18

Input:
B = [[-3, -3, 1, -4, 2], [4, -3, -5, 2, 1], [4, 2, 2, 1, 3], [-1, -5, -3, 5, -4], [-3, -3, 5, -2, -3]]

Output:
42
'''

board = eval(input()[4:])
result = 0

for row in range(len(board)):
    for col in range(len(board)):
        if board[row][col] < 0:
            result += -(board[row][col])


print(result)
