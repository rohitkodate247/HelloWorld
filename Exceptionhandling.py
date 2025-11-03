# Using Multiple except Blocks
try:
    with open("file.txt", "r") as file:
        data = file.read()
        result = int(data) / 2
except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("File content is not a valid number.")
except ZeroDivisionError:
    print("Division by zero error!")

# Using else Block
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You cannot divide by zero!")
else:
    print("The result is:", result)

# Using finally Block
try:
    file = open("file.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing the file.")
    # file.close()  # Ensures resources are released
