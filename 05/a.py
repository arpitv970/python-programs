myStr = str(input('Enter String: '))

if (myStr == myStr[::-1]):
    print(f'{myStr} is a pallindrome')
else:
    print(f'{myStr} is not a pallindrome')
