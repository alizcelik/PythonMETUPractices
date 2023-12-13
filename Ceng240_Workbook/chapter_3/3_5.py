'''
Write a function named find_median that takes a list of integers as the distribution of the grades and returns an integer as the median of this distribution. If the list has an even length, the function must return the higher of the two middle elements.

Hint: You can use the built-in function  sorted()
  to get the grades in the increasing order.

#>>> find_median([72,32,49,20,33])
33

#>>> find_median([27,48,9,63,99,61,33,80,43,84,39,46,40,46,16,55,69,43,11,57])
46
'''


def find_median(numbers):
    numbers = sorted(numbers)
    size = len(numbers)
    mid = int()
    if size % 2 == 0:
        mid = int((size + 1) / 2)
    else:
        mid = int(size / 2)
    return numbers[mid]

print(find_median([72,32,49,20,33]))
print(find_median([27,48,9,63,99,61,33,80,43,84,39,46,40,46,16,55,69,43,11,57]))