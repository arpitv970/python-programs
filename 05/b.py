text = str(input('Enter Text: '))

words = text.split()

cCount = 0    # character count
bCount = len(words) - 1    # blank count
vCount = 0    # vowel count

v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for i in words:
    cCount += len(i)

    for j in i:
        if (j in v):
            vCount += 1

print(f'No. of characters: {cCount}')
print(f'No. of blanks: {bCount}')
print(f'No. of vowels: {vCount}')
