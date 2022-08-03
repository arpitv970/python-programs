n = str(input('Enter number: '))

if (n == n[::-1]):
    print(f'{n} is a palindrome number')

else:
    print(f'{n} is not a palindrome number')
