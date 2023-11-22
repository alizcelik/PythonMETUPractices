"""
2.9. Exercise: Office Olympics 2
It’s Office Olympics time! Jim is trying to find the medalists by finding the three people that have the highest scores.
 Can you help him find the three people who have the most wins?

Write a program that takes a list of 2-tuples which consists of a string and an integer representing the name of people
 and their score and prints a list of 3 strings which are the names of 3 winners. You can assume that there are always at least three contestants in the Olympics.

Sample I/O:

Input:
wins_list = [("jim", 11), ("pam", 9), ("dwight", 12), ("oscar", 2), ("micheal", 17), ("angela", 3), ("kevin", 1)]

Output:
["micheal", "dwight", "jim"]

Input:
B = [("jim", 1), ("pam", 4), ("jan", 10), ("creed", 7), ("micheal", 5), ("meredith", 2), ("phyllis", 28)]

Output:

["phyllis", "jan", "creed"]
"""

competitors = input()
competitors_list = eval(competitors[competitors.find('=')+2:])
#
# winners=list()
# for row in competitors_list:
#     max_score =0
#     max_index = 0
#     for i in range(3):
#         if competitors_list[row][1] > max_score:
#             max_score = competitors_list[row][1]
#             max_index = row
#
#     print(competitors_list)


sorted_list = sorted(competitors_list, key=lambda x: x[1], reverse=True)

# Extract the names of the top 3 winners
top_three_winners = [name for name, score in sorted_list[:3]]

print(top_three_winners)

