'''
ENDING MACHINE (VM)

You are to implement a program that simulates a vending machine (VM). Your program will read three pieces of data in the following order:

A dictionary, representing the current stock of the VM. The keys of the dictionary are item names (as strings) and the prices as integers. You can assume the stock is limitless for the items in the VM. E.g.:

{"chocolate": 2, "spring_water": 1, "energy_drink": 7}

A list of strings, representing the items requested by the customer. Repeating an item's name means requesting a second from that item, e.g.:

["energy_drink", "chips", "chocolate", "chocolate"]

If a requested item is not in the VM, your VM should ignore it.

An integer, representing the amount of money inserted by the customer.

After these three inputs, your VM should calculate the total price of the items requested and should print one of the following:

"Change:X" if the money inserted is higher than the total price of the requested items. The integer X is the amount of money that the customer needs to get back.

"Insert:X" if the money inserted is less than the total price of the requested items. The integer X is the amount of extra money that the customer needs to insert.

"Done", if the inserted money and the total price of the requested items are equal to each other.

Any output that does not follow this output format (in terms of lowercase and uppercase letter as well as the spacing) will be graded zero.

Hints:

Hint 1: You can use eval(input()) to read the provided dictionary and list directly.

Hint 2: If needed, you can use <dictionary>.keys() to get the keys of the dictionary.

Example I/O:

==================

Input 1:

{"chocolate": 2, "spring_water": 1, "energy_drink": 7}

["energy_drink", "chocolate"]

20

Output 1:

Change:11

==================

Input 2:

{"chocolate": 2, "spring_water": 1, "energy_drink": 7, "coke":5}

["coke", "coke", "coke", "chips", "candy", "chocolate"]

15

Output 2:

Insert:2

==================

Input 3:

{"chocolate": 2, "spring_water": 1, "energy_drink": 7, "coke":5, "hand_sanitizer": 5}

["hand_sanitizer", "mask"]

5

Output 3:

Done

==================
'''

products = eval(input())
orders = eval(input())
inserted_money=int(input())


price = int()

for key, value in products.items():
    for order in orders:
        if order == key:
            price += value

if price < inserted_money:
    print("Change:" + str(inserted_money - price))
elif price == inserted_money:
    print("Done")
else:
    print("Insert:" + str(price - inserted_money))

vending_machine = eval(input())
requests = eval(input())
inserted_money = int(input())

valid_requests = [req for req in requests if req in vending_machine.keys()]
