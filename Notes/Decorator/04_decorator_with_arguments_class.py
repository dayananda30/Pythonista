def decoratorfactory(message):
    class Decorator:
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            print("Decoratored Function - {}".format(message))
            return self.func(*args, **kwargs)

    return Decorator


@decoratorfactory("Hello Daya")  # This is equaivalent to my_function = my_decorator(my_function)
def my_functions():
    print("My ordinary Function")


my_functions()
