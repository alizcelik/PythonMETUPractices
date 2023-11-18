
#list of courses
courses = ['History', 'Math', 'Physics', 'CompSci']
optional_courses = ['Education', 'Sociology']
grades= [5,3,1,4,2]

#access an element
print('0 ->' +courses[0])
print('-1 ->' + courses[-1])

#sub array
print(courses[1:3])
print(courses[:3])
print(courses[2:])

#add item
courses.append('Art')

print(courses)

#add item exact index
courses.insert(0,'Chem')

print(courses)

#remove an element
courses.remove('Math')

print(courses)

#remove with pop
popped = courses.pop()

print(courses)
print(popped)
#migrate list
courses.extend(optional_courses)

print(courses)

#reverse list
courses.reverse()

print(courses)

#sorting list
	#ascending order
courses.sort()
grades.sort()

print(courses)
print(grades)

	#descending order

courses.sort(reverse=True)
grades.sort(reverse=True)

print(courses)
print(grades)

	#sorted
sorted_courses = sorted(courses)

print(sorted_courses)

#max-min-sum of list
print(max(grades))

print(min(grades))

print(sum(grades))

#find index
print(courses.index('CompSci'))

#availablity
print('Art' in courses)

print('CompSci' in courses)

#
for item in courses:
	print(item)

#enumarate
for index, item in enumerate(courses):
	print(index, item)

#starting number for index
for index, item in enumerate(courses, start=2):
	print(index, item)

#list to string
course_str = '-*-'.join(courses)

print(course_str)
print("Line 98")

#
new_list = course_str.split('-*-')

print(new_list)

#Tuples are immutable
#Lists are mutable


#sets
#sets do not let duplicates
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'CompSci'}
print(cs_courses)

print('Math' in cs_courses)

#common elements
print(cs_courses.intersection(art_courses))

#diff elements
print(cs_courses.difference(art_courses))

#migrate-unite
print(cs_courses.union(art_courses))

#empty list
empty_list = []
empty_list = list()

#empty tuples
empty_tuple = ()
empty_tuple = tuple()

#empty sets
#empty_set = {} -> not correct
empty_set = set()



