def isPrime(n):
    for i in range(2, n):
        if (n % i == 0):
            return False
        else:
            return True

n = int(input('Enter number: '))

for i in range(1, n + 1):
    if(isPrime(i)):
        print(i)
