'''
A group of people wants to make a little trip to another city by train and also calculate the total ticket price because ticket prices are different with respect to age. In this question, you will write a program that reads the ages of the each person in the group and calculate the total ticket price and then print it. Please note that the people count is unknown and input includes all the ages in one line seperated by one space.
Ticket prices with respect to ages are as follows:
- 0-10  →
  30
- 11-25  →
  60
- 26-60  →
  90
- 60<  →
  50
Sample I/O:

Input:
[35, 35, 5, 15]

Output:
270

Input:
23 25

Output:
120

Input:
[57, 63, 1, 2, 4, 6, 8, 10, 15]

Output:
380

Input:
[33]

Output:
90
'''

ages = eval(input())
price = int()

for age in ages :
    if age > 60:
        price += 50
    elif age > 25:
        price += 90
    elif age > 10:
        price += 60
    elif age >= 0:
        price += 30

print(price)
