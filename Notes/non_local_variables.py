"""
    nonlocal is used to indicate that a variable is a local variable of an enclosing (non-global)
            scope.
    It is typically used inside nested functions to modify the value of a variable in the nearest
            enclosing scope that is not global.
    It allows you to work with variables in outer functions without creating a new local variable
            in the current function.
"""


def counter():
    x = 0

    def increment_counter():
        nonlocal x  # without this line, you get unbound local variable exception
        x = x + 1
        print(x)
        return x

    return increment_counter


c = counter()
c()
c()
c()
