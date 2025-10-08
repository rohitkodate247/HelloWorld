# Task: Manage test execution order

from collections import deque

# Create a queue (FIFO)
test_queue = deque(["TC_001", "TC_002", "TC_003"])
print("Initial Queue:", test_queue)

# Process tests in FIFO order
while test_queue:
    current_test = test_queue.popleft()  # removes first element
    print("Running:", current_test)

# Stack (LIFO)
test_stack = ["TC_004", "TC_005", "TC_006"]
print("\nInitial Stack:", test_stack)

while test_stack:
    current_test = test_stack.pop()  # removes last element
    print("Running:", current_test)

# Explanation:
# deque → Double-ended queue from collections library; faster for pop/append.
# .popleft() → Removes items from the front (FIFO behavior).
# .pop() → Removes from the end (LIFO behavior).
