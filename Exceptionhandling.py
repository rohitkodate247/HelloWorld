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
