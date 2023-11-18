original_tuple = eval(input())          # *see below for explanation
index, missing_number = eval(input())   # notice tuple matching

lst = list(original_tuple)              # cast tuple to list so that you can change
lst[index] = missing_number

recovered_tuple = tuple(lst)            # cast list back to tuple again.

print(recovered_tuple)

"""*This is a tricky way to get a tuple or a list from the user.
It's not very safe but it is easy to do so for now.
You will learn the more proper way to this later."""