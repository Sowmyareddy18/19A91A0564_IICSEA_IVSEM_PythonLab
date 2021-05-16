#Implement a python script to compute distance between two points taking input from the user (Pythagorean Theorem).
import math
x1=int(input('enter x1 '))
y1=int(input('enter y1 '))
x2=int(input('enter x2 '))
y2=int(input('enter y2 '))
distance=math.sqrt((x2-x1)**2)+((y2-y1)**2)
print('Distance between points (x1,y1) and (x2,y2) is:',distance)
#output:
enter x1 0
enter y1 0
enter x2 6
enter y2 8
Distance between points (x1,y1) and (x2,y2) is: 10.0
