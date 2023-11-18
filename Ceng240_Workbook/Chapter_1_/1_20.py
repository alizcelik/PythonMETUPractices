'''
You live in a city called Pawnee, and you share this beautiful city with citizens that are really bad at spelling words. This town’s slogan is “When you’re here, then you’re home.” but your fellow citizens keep spelling “then” as “than”.

Given a misspelled slogan, fix the typo and print the correctly spelled slogan.

Since this is a question to practice, please try to manipulate the string itself, rather than directly printing the correct city slogan.

Sample I/O:

Input:
When you're here, than you're home.

Output:
When you're here, then you're home.
'''

slogan=str(input())

index=slogan.find('then')
if index >= 0:
    slogan.replace('then','than')

print(slogan)