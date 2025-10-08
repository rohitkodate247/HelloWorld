# Task: Represent a chain of test steps

# Define a Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # pointer to the next node


# Create linked list nodes
step1 = Node("Initialize")
step2 = Node("Run Test")
step3 = Node("Collect Results")

# Link the nodes
step1.next = step2
step2.next = step3

# Traverse the linked list
current = step1
while current:
    print("Step:", current.data)
    current = current.next

# Explanation:
# A linked list is made of nodes pointing to the next node.
# Each Node has data and a next reference.
# Traversal continues until current.next becomes None.
