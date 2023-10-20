"""
    a decorator is a function that can be applied to another function to augment its
    behavior. The syntactic sugar is equivalent to the following: my_func = decorator(my_func).

     But what if the decorator was instead a class? The syntax would still work, except that now my_func gets
     replaced with an instance of the decorator class. If this class implements the __call__() magic method,
     then it would still be possible to use my_func as if it was a function
"""


class my_decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("before the function call")
        res = self.func(*args, **kwargs)
        print("After the function call")
        return res


@my_decorator
def my_function():
    print("My ordinary Function!")


my_function()
# before the function call
# My ordinary Function!
# After the function call
