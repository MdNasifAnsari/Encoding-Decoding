from encoding import encoding
from decoding import decoding

while True:
    print("\n===== CODING-DECODING APP =====")
    print("1. Encoding")
    print("2. Decoding")
    print("0. Exit")

    try:
        opt = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if opt == 1:
        encoding()

    elif opt == 2:
        decoding()

    elif opt == 0:
        print("Thank you for using the app!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 0.")
