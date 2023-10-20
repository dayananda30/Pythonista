foo = 1


def func():
    bar = 2
    foo = "I am local"
    print(globals().keys())  # prints all variable names in global scope
    print(locals().keys())  # prints all variable names in local scope

    # global variable foo still exists, unchanged:
    print(globals()['foo'])  # prints 1
    print(locals()['foo'])  # prints 2


func()
