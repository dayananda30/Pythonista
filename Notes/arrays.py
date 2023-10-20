"""
Arrrays are similar to Lists but contains only homogeneous data types.

Parameters:
c - Represents character of size 1 byte
i - Represents signed integer of size 2 bytes
f - Represents floating point of size 4 bytes
d - Represents floating point of size 8 bytes
"""
from array import *

# Access individual elemets through indexes
my_array = array('i', [1, 2, 3, 4, 5, 6])
print(my_array[2])
# 3

# Append values
my_array.append(7)
print(my_array)
# array('i', [1, 2, 3, 4, 5, 6, 7])


# Insert values
my_array.insert(0, 0)
print(my_array)
# array('i', [0, 1, 2, 3, 4, 5, 6, 7])


# Extend arrays
tmp_array = array('i',[8,9])
my_array.extend(tmp_array)
print(my_array)
# array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Add List into array
my_list = [10,11]
my_array.fromlist(my_list)
print(my_array)
# array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

