number = int(input("Enter an integer: "))

if number < 2:
    print("The number is not a prime number.")
else:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("The number is a prime number.")
    else:
        print("The number is not a prime number.")