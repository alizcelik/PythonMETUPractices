'''
In our letter grade system, our total point obtained in a course is converted to a letter grade. In this question, you will write a program that reads the total point from the user and prints the corresponding letter grade.
Total point intervals and their letter grade equivalents:
- 90-100  →
  AA
- 85-89  →
  BA
- 80-84  →
  BB
- 75-79  →
  CB
- 70-74  →
  CC
- 65-69  →
  DC
- 60-64  →
  DD
- 50-59  →
  FD
- 0-49  →
  FF
Sample I/O:

Input:
50

Output:
FD

Input:
71

Output:
CC

Input:
89

Output:
BA
'''

grade = int(input())

if grade > 89 :
    print('AA')
elif grade > 84 :
    print('BA')
elif grade > 79 :
    print('BB')
elif grade > 74 :
    print('CB')
elif grade > 69 :
    print('CC')
elif grade > 64 :
    print('DC')
elif grade > 59 :
    print('DD')
elif grade > 49 :
    print('FD')
else:
    print('FF')