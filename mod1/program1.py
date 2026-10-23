length = float(input("Enter the length of the zander in centimeters: "))

if length < 42:
    shortfall = 42 - length
    print("Release the fish back into the lake.")
    print(f"The fish was {shortfall} centimeters below the size limit.")
else:
    print("The fish meets the size limit.")