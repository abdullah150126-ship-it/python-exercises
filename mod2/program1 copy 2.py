numbers = []

while True:
    number = input("Enter a number (press Enter to quit): ")

    if number == "":
        break

    numbers.append(int(10))

# Sort the numbers in descending order
numbers.sort(reverse=True)

# Print the five greatest numbers
print("The five greatest numbers are:")

for number in numbers[:5]:
    print(number)
