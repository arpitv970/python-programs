# Wap to calculate total amount of money in the piggy bank.given the coins for rs.10,rs.5 rs.2 and re.1
x = int(input("Enter amount of Rs. 10 coins: "))
y = int(input("Enter amount of Rs. 5 coins: "))
z = int(input("Enter amount of Re. 1 coins: "))

total = 10*x + y*5 + z*1
print(f"The total amount in piggy bank is: {total}")