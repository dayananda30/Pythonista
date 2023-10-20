"""
Syntax:

    [ <expression> for <element> in <iterable> ]
    [ <expression> for <element> in <iterable> if <condition> ]

"""

squares = [x * x for x in [1, 2, 3, 4, 5]]
print(squares)

# examples:
# Get a list of uppercase characters from a string
[s.upper() for s in "Hello World"]
# ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']
# Strip off any commas from the end of strings in a list
[w.strip(',') for w in ['these,', 'words,,', 'mostly', 'have,commas,']]
# ['these', 'words', 'mostly', 'have,commas']


# When using if/else together use them before the loop
res = [x if x in 'aeiou' else '*' for x in 'apple']
print(res)
# ['a', '*', '*', '*', 'e']

# double iteration
foo = [1, 2, 3, 4, 5]
res = [str(x) for i in range(3) for x in foo(i)]
print(res)
