# Task: Read a CSV and find failed tests

import csv

# Example CSV format:
# TestID,Result
# TC_001,PASS
# TC_002,FAIL
# TC_003,PASS


def find_failed_tests(filename):

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        failed_tests = [row["TestID"]
                        for row in reader if row["Result"] == "FAIL"]
    return failed_tests


print(find_failed_tests("test_results.csv"))

# Explanation:
# csv.DictReader reads each line as a dictionary ({"TestID": ..., "Result": ...}).
# List comprehension filters tests where "Result" equals "FAIL".
# The with open() block ensures the file closes automatically.
