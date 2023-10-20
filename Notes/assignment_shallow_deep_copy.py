"""
https://towardsdatascience.com/assignment-shallow-or-deep-a-story-about-pythons-memory-management-b8fad87bfa6c

Assignment:
    When you use a simple assignment in Python, you are creating a new reference to the same object in memory. Both the
    original variable and the assigned variable will refer to the same object. Any changes made to the object through one
    variable will be reflected in the other since they both point to the same object.


B = A

B -> [           ]
      | | | | | |
A -> [1,2,3,4,5,6]


"""

original_list = [1, 2, 3]
assigned_list = original_list
original_list[0] = 100
print(assigned_list)  # Output: [100, 2, 3]


"""
Shallow Copy:
    A shallow copy creates a new object, but it doesn't create copies of nested objects within the original object. 
    Instead, it copies references to these nested objects. Changes to the top-level elements are independent between the 
    original and the shallow copy. However, changes to nested objects (e.g., elements of a list within a list) will 
    affect both the original and the shallow copy. 
    
B = A

A -> [           ]
      | | | | | |
     [1,2,3,4,5,6]
      | | | | | |
B -> [           ]
    """

import copy
original_list = [1, [2, 3]]
shallow_copy = copy.copy(original_list)
original_list[1][0] = 100
print(shallow_copy)  # Output: [1, [100, 3]]
