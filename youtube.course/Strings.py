
message = 'Hello World'

print(message)

#length of string
print(len(message))

#last character
print(message[10])

#substring
print(message[0:5])

#from first
print(message[:5])

#till end
print(message[6:])

#lower case
print(message.lower())

#upper case
print(message.upper())

#search count
print(message.count('Hello'))

#find index
print('find index')
print(message.find('World'))
print(message.find('xyz'))

#replace
new_message = message.replace('World', 'Universe')
print(new_message)

#concat
greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name
print(message)


#format
#1
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

#2
message = f'{greeting}, {name.upper()}. Welcome! Heyyy.'
print(message)

#you can see methods with dir
#print(dir(message))

#help function
#print(help(str))

#print(help(str.lower))


