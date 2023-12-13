'''
Write a function named find_first_non_prime to find the first non-prime number in the given list. If all the numbers are prime, return False.

Hint: You can define a helper function to determine whether a number is prime or not then use it in your function.

Sample I/O:

>>> find_first_non_prime([2,3,4,7])
4

>>> find_first_non_prime([2,3,5,7])
False

>>> find_first_non_prime([2,3,51,19])
51
'''


def find_first_non_prime(numbers):
    for number in numbers:
        num = number -1
        isPrime = True
        while num >= 2:
            if number % num == 0:
                isPrime = False
            num -= 1
        if isPrime != True:
            return number
    return False