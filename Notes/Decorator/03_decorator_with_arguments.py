def decoratorfactory(message):
    def my_decorator(f):
        def inner(*args, **kwargs):
            print("My decorated Function - {}".format(message))
            return f(*args, **kwargs)

        return inner
    return my_decorator


@decoratorfactory("Hello Daya")  # This is equaivalent to my_function = my_decorator(my_function)
def my_functions():
    print("My ordinary Function")


my_functions()
