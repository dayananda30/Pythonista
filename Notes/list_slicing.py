
# Using the third "step" argument
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(lst[::2])
# Output: ['a', 'c', 'e', 'g']
print(lst[::3])
# Output: ['a', 'd', 'g']


#  Selecting a sublist from a list
lst = ['a', 'b', 'c', 'd', 'e']
print(lst[2:4])
# Output: ['c', 'd']
print(lst[2:])
# Output: ['c', 'd', 'e']
print(lst[:4])
# Output: ['a', 'b', 'c', 'd']

# Reversing a list with slicing
a = [1, 2, 3, 4, 5]
# steps through the list backwards (step=-1)
b = a[::-1]
# built-in list method to reverse 'a'
a.reverse()
