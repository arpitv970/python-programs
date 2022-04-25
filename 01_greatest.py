# Wap to find greatest of three numbers

def grtest(x, y, z):
    if (x >= y and x >= z):
        return x
    elif (y >= x and y >z):
        return y
    else:
        return z

a, b, c = input('Enter values of a, b, c: ').split()
print(f"greatest among {a}, {b}, {c} is: {grtest(a, b, c)}")