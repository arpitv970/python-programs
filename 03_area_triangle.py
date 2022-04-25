# Area of triangle using heron's formula

print('Enter the dimensions of triangle:')
a = int(input('Side 1: '))
b = int(input('Side 2: '))
c = int(input('Side 3: '))

s = (a + b + c)/2

area = (s*(s-a)*(s-b)*(s-c))**(0.5)
print(f"The area is: {area}")