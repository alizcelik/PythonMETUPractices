'''
Cartman wants to eat some sushi. So, he goes to City Sushi. The menu has  N
  sushis in it, with indexes starting from 1, and he has the prices of them as a list of integers.
  He would like to choose sushis between a starting and an ending index.

Write a function named total_price that takes a list of integers as the prices of sushis,
and two integers as the starting and ending index of the selection (with the ending index excluded).
The function must return the total cost of selected sushis as an integer.

Input:

>>> total_price([1, 5, 2, 6, 12, 5, 23, 15], 2, 6)
25

Input:

>>> total_price([7, 7, 7, 5, 6, 3, 5, 7, 8], 1, 9)
47
'''
'''
def total_price(prices, order_1, order_last):
    order = prices[order_1:order_last]
    total = sum(order)
    return total
'''
def total_price(prices, l, r):
    total_cost = 0
    for i in range(l-1, r-1):
        total_cost += prices[i]
    return total_cost
