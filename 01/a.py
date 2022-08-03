a, b, c = input('Enter values of a, b, c: ').split()

if (a >= b and a >= c):
    print(f'Greatest: {a}')
elif (b >= a and b >= c):
    print(f'Greatest: {b}')
else:
    print(f'Greatest: {c}')
