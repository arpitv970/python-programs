# Calculate distance between two points
from dis import dis
from math import dist
from turtle import distance


x1 = int(input('Enter coordinate x1: '))
y1 = int(input('Enter coordinate y1: '))
x2 = int(input('Enter coordinate x2: '))
y2 = int(input('Enter coordinate y2: '))

distance = ((x2 - x1)**2 + (y2 - y1)**2)**(0.5)
print(f"The distance b/w points is: {distance}")