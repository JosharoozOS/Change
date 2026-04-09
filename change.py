# Author: Josh Hein
# GitHub username: JosharoozOS
# Date: 4/8/2026
# Description: We are creating a system that calculates the coind you give when giveing change.

cents = int(input("Please enter an amount in cents less than a dollar.\n"))

quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents

print("Your change will be:")
print(f"Q: {quarters}")
print(f"D: {dimes}")
print(f"N: {nickels}")
print(f"P: {pennies}")
