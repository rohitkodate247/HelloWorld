# practice pytest
import copy
# Shallow Copy
original_list = [1, 2, [3, 4]]
shallow_copied_list = copy.copy(original_list)

shallow_copied_list[2][0] = 'Changed'
print(original_list)  # Output: [1, 2, ['Changed', 4]]

# Deep Copy
original_list = [1, 2, [3, 4]]
deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2][0] = 'Changed'
print(original_list)  # Output: [1, 2, [3, 4]]
print(deep_copied_list)  # Output: [1, 2, ['Changed', 4]]
