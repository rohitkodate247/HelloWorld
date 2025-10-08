# Task: Store test results as key-value pairs

# Dictionary to store test case results
test_results = {
    "TC_001": "PASS",
    "TC_002": "FAIL",
    "TC_003": "PASS"
}

# Access and print specific test result
print("Result of TC_002:", test_results["TC_002"])

# Iterate through dictionary
for test_id, result in test_results.items():
    print(f"{test_id} => {result}")

# Explanation:
# {} → Creates a dictionary (hash map) with keys (test IDs) and values (results).
# .items() → Returns both key and value for iteration.
# f"{test_id} => {result}" → f-string for clean formatted output.
