# Author: Josh Hein
# GitHub username: JosharoozOS
# Date: 4/8/2026
# Description: We are creating a system that calculates the coind you give when giveing change.

print("Please enter an amount in cents less than a dollar.")
userInput = int(input())


print("Your change will be:")

quarter = 25
q = int(userInput/quarter)
print("Q: ", q)
print()
remainder = userInput % quarter

dime = 10
d = int(remainder/dime)
print("D: ", d)
print()
remainder = remainder % dime

nickel = 5
n = int(remainder/nickel)
print("N: ", n)
print()
remainder = remainder % nickel

penny = 1
p = int(remainder/penny)
print("P: ", p)
