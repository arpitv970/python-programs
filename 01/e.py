n = int(input('Enter number: '))

ans = 0

while (n != 0):
    ans = (10 * ans) + (n % 10)
    n //= 10

print(ans)
