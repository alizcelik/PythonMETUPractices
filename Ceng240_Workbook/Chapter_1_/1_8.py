'''
A student is jogging on the tracks at the Devrim Stadium. This jogging session is divided into 4 intervals. Given the average speed (in meters per second) and duration of the interval (in seconds) for each of the 4 intervals and the length of one lap (i.e. distance around the running track, in meters) calculate and print the number of laps the student has taken during his/her jogging session as a float. (1 digit after the decimal point is sufficient)

Inputs will be given as floats in the following order:

Average speed for 1st interval

Duration of 1st interval

Average speed for 2nd interval

Duration of 2nd interval

Average speed for 3rd interval

Duration of 3rd interval

Average speed for 4th interval

Duration of 4th interval

Length of one lap

Sample I/O:

Input:
6
420
5.5
240
7
300
3.5
180
400

Output :
16.4

Input:
4.2
300
5.9
240
7.8
260
4.4
200
420

Output:
13.3

'''

speed1=float(input())
duration1=float(input())
speed2=float(input())
duration2=float(input())
speed3=float(input())
duration3=float(input())
speed4=float(input())
duration4=float(input())
lap_length=float(input())

total_length=(speed1*duration1)+(speed2*duration2)+(speed3*duration3)+(speed4*duration4)
total_lap=total_length/lap_length
print(round(total_lap,1))



