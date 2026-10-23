airports = {}

while True:
    print("\nChoose an option:")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        icao = input("Enter the ICAO code: ")
        name = input("Enter the airport name: ")
        airports[icao] = name
        print("Airport added.")

    elif choice == "2":
        icao = input("Enter the ICAO code: ")

        if icao in airports:
            print(airports[icao])
        else:
            print("Airport not found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")