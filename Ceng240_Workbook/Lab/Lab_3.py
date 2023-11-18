'''

- Encoding for the flower name is as such:

          • If the most significant digit (the leftmost digit) of the first number is 7, the requested flower is Rose,
          • if the most significant digit (the leftmost digit) of the first number is 8, the requested flower is Tulip,
          • otherwise the requested flower is Orchid.

- Encoding for the color is as such:

          • If the least significant digit (the rightmost digit) of the second number is 0, 1, 2 or 3 the color is White,
          • if the least significant digit (the rightmost digit) of the second number is 4, 5 or 6 the color is Pink,
          • if the least significant digit (the rightmost digit) of the second number is 7, 8 or 9 the color is Red.

- There is no actual encoding for the number of flowers. The third number will directly be the number of flowers ordered by the customer. However, there are such restrictions about flower amounts:

          • At most 100 Roses can be ordered at once. If more than 100 Roses are requested, the order is Invalid.
          • At most 50 Tulips can be ordered at once. If more than 50 Tulips are requested, the order is Invalid.
          • At most 30 Orchids can be ordered at once. If more than 30 Orchids are requested, the order is Invalid.

- At the end, you will print the order information as such:

          • If the order is invalid, you will print "Invalid!"
          • If the order is valid, you will print flower name, flower color and the amount without spaces. For example for 10 pink roses you will print "RosePink10". (Yes, flower name and the color will start with uppercase letters.)

          Example I/O:

Input1:
7
4
90

Output1:
RosePink90

Input2:
85012012
23
40

Output2:
TulipWhite40

Input3:
13
301
40

Output3:
Invalid!

* Input3 is invalid since it requests 40 white orchids but maximum permitted amount for orchids is 30.

'''


input_1 = str(input())
flower_num = int(input_1[0])
output = str()

input_2 = str(input())
color_num = int(input_2[len(input_2) - 1])

input_3 = str(input())
count = int(input_3)

if flower_num == 7:
    output = 'Rose'
elif flower_num == 8:
    output = 'Tulip'
else:
    output = 'Orchid'


if color_num <= 3:
    output += 'White'
elif color_num <= 6:
    output += 'Pink'
else:
    output += 'Red'

output += str(count)

if count > 100 and flower_num == 7:
    output = 'Invalid!'
elif count > 50 and flower_num == 8:
    output = 'Invalid!'
elif count > 30 and flower_num != 7 and flower_num != 8:
    output = 'Invalid!'

print(output)



