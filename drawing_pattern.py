# 🖼️ Python Pattern Drawing Project
from colorama import Fore, Style

while True:

    # Step 1: Display a menu to the user

    print("🌟 Welcome to the Python Pattern Drawing Program!")
    print("Choose a pattern type:")
    print("1. Right-angled Triangle")
    print("2. Square with Hollow Center")
    print("3. Diamond")
    print("4. Left-angled Triangle")
    print("5. Hollow Square")
    print("6. Pyramid")
    print("7. Reverse Pyramid")
    print("8. Rectangle with Hollow Center")
    print("9. Red and Blue Checkerboard")
    print("10. Half Diamond")

    # Step 2: Get the user's choice

    choice = int(input("Enter the number corresponding to your choice: "))

    # Step 3: Get dimensions based on choice

    if choice in [1, 3, 4, 6, 7, 9, 10]:  # Patterns that need the number of rows
        rows = int(input("Enter the number of rows: "))
    elif choice in [2, 5]:  # Patterns that need size
        size = int(input("Enter the size of the square/rectangle: "))
    elif choice == 8:
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))

    # Step 4: Generate the selected pattern

    if choice == 1:  # Right-angled Triangle
        # Loop through rows and print increasing stars
        for i in range(1, rows + 1):
            print("*" * i)

    elif choice == 2:  # Square with Hollow Center
        # Create a square with a hollow center

        # My first try to do a square pattern :)
        for i in range(1, size + 1):
            if i == 1:
                print(Fore.MAGENTA + "*" * size)
            elif i == size:
                print(Fore.MAGENTA + "*" * i)
            else:
                print(Fore.MAGENTA + "*".ljust(size - 2), "*")

    elif choice == 3:  # Diamond
        # Create a diamond shape using loops
        for i in range(rows):
            for j in range(rows - i - 1):
                print(" ", end="")
            for j in range(0, i + 1):
                print(Fore.GREEN + "* ", end="")
            print()

        for i in range(rows):
            for j in range(i + 1):
                print(" ", end="")
            for j in range(0, rows - i - 1):
                print(Fore.GREEN + "* ", end="")
            print()

    elif choice == 4:  # Left-angled Triangle
        # Print decreasing stars for each row
        for i in range(rows, -1, -1):
            print("*" * i)

    elif choice == 5:  # Hollow Square
        # Similar to choice 2 but ensure perfect square logic

        # After few tries and some research in google...
        for i in range(size):
            for j in range(size):
                if i == 0 or i == (size - 1):
                    print("*", end="")
                else:
                    if j == 0 or j == (size - 1):
                        print("*", end="")
                    else:
                        print(" ", end="")
            print()

    elif choice == 6:  # Pyramid
        # Center-align stars to form a pyramid
        for i in range(rows):
            for j in range(0, rows - i - 1):
                print(" ", end="")
            for k in range(0, i + 1):
                print(Fore.YELLOW + "* ", end="")
            print()

    elif choice == 7:  # Reverse Pyramid
        # Create an upside-down pyramid
        for i in range(rows):
            for j in range(i + 1):
                print(" ", end="")
            for k in range(0, rows - i - 1):
                print(Fore.BLUE + "* ", end="")
            print()

    elif choice == 8:  # Rectangle with Hollow Center
        # Handle separate width and height inputs for rectangle
        for i in range(height):
            for j in range(width):
                if i == 0 or i == (height - 1):
                    print(Fore.RED + "*", end="")
                elif i != 0:
                    if j == 0 or j == (width - 1):
                        print(Fore.RED + "*", end="")
                    elif j != 0:
                        print(" ", end="")

            print()

    elif choice == 9:  # Draw red and blue checkerboard
        # My own interpretation of a checkerboard
        for i in range(1, rows + 1):
            if i % 2 != 0:
                for j in range(1, rows + 1):
                    if j % 2 != 0:
                        print(Fore.BLUE + "o ", end="")
                    elif j % 2 == 0:
                        print(Fore.RED + "o ", end="")
                print()
            elif i % 2 == 0:
                for j in range(1, rows + 1):
                    if j % 2 != 0:
                        print(Fore.RED + "o ", end="")
                    elif j % 2 == 0:
                        print(Fore.BLUE + "o ", end="")
                print()

    elif choice == 10:  # Draw Half Diamond
        # Just another shape
        for i in range(1, rows + 1):
            print(Fore.CYAN + "*" * i)

        for k in range(rows - 1, 0, -1):
            print(Fore.YELLOW + "*" * k)

    else:
        print("❌ Invalid choice! Please restart the program.")

    # Step 5: Allow the user to restart or exit

    user_input = input(Style.RESET_ALL + "Pess ANY key to restart or 'X' to exit: ").capitalize()

    if user_input == "X":
        break

