# Task: Store and process ordered test IDs

# Create a list of test IDs
test_ids = ["TC_001", "TC_002", "TC_003", "TC_002"]

# Print all test IDs
print("All test IDS:", test_ids)

# Find duplicates
duplicates = [tid for tid in test_ids if test_ids.count(tid) > 1]
print("Duplicate test IDs:", set(duplicates))

# Explanation:
# test_ids = [...] → Creates an ordered list of test case identifiers.
# .count(tid) → Counts how many times each element appears.
# The list comprehension [tid for tid in test_ids if ...] → filters duplicates.
# set(duplicates) → Converts the list to a set to remove repeated duplicates.
