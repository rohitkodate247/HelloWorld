# practice pytest
def classify_grade(score):
    # Check if score is within valid range
    if not (0 <= score <= 100):
        return "Invalid score"

    # Determine grade based on score range
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# --- Main program with user input ---
try:
    # Take input and convert to integer
    score = int(input("Enter the student's score (0-100): "))
    # Print classification result
    print("Grade:", classify_grade(score))
except ValueError:
    # Handle non-numeric input
    print("Invalid input. Please enter a numeric score.")
