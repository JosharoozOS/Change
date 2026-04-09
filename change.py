# Author: Josh Hein
# GitHub username: JosharoozOS
# Date: 4/8/2026
# Description: We are creating a system that calculates the coind you give when giveing change.

print("Please enter an amount in cents less than a dollar.")
userInput = int(input())
print()

print("Your change will be:")

quarter = 25
print("Q: ", int(userInput/quarter))
remainder = userInput % quarter

dime = 10
print("D: ", int(remainder/dime))
remainder = remainder % dime

nickel = 5
print("N: ", int(remainder/nickel))
remainder = remainder % nickel

penny = 1
print("P: ", int(remainder/penny))
