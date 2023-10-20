# Any and All
# You can use all() to determine if all the values in an iterable evaluate to True

nums = [1, 1, 0, 1]
all(nums)
# False
chars = ['a', 'b', 'c', 'd']
all(chars)
# True


# Likewise, any() determines if one or more values in an iterable evaluate to True
nums = [1, 1, 0, 1]
any(nums)
# True
vals = [None, None, None, False]
any(vals)


# Initializing a List to a Fixed Number of Elements

my_list = [None] * 10
my_list = ['test'] * 10

print(my_list)
