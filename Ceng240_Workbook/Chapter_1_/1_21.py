'''
Programming assignments in the hypothetical CENG314 course forms 5% of the total grade. There are 5 programming assignments, each graded over 10. Only the highest 4 grades taken from these assignments are taken into consideration, i.e. the assignment with the lowest grade is ignored.
You need to write a program that asks the grades obtained from each assignment and prints the total grade contribution from the programming assignments in this course.
Consider a student with grades 8, 9, 4, 3, 3. We ignore one of the 3’s. The student has obtained a sum of 24 over 40, which computes as 3 over 5. The output will be 3.

Hint: You might want to use the function  min()
 . It takes a list, or at least two arguments and returns the least element.

Sample I/O:

Input:
8
9
4
3
3

Output:
3.0

Input:
10
5
6
3
7

Output:
3.5
'''
grades=[]

for i in range(5):
    grades.append(int(input()))

minOf=min(grades)
grades.remove(minOf)
sumOf=sum(grades)
print(round(sumOf/8, 1))
