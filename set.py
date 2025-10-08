# Task: Store only unique error codes

# Set of unique error codes
error_codes = {"E101", "E102", "E101", "E103"}

# Sets automatically remove duplicates
print("Unique error codes:", error_codes)

# Add a new error code
error_codes.add("E104")
print("Updated error codes:", error_codes)


# Explanation:
# {} with values → Creates a set (no duplicate elements).
# .add() → Adds new elements.
# Useful when you only care about unique values (e.g., distinct error IDs).
