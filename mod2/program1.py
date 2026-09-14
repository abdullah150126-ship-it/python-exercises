import random

dice = int(input("How many dice to roll? "))

total = 0

for _ in range(dice):
    roll = random.randint(1, 6)
    total += roll

print("Sum:", total)