x = "I am global variable"


def read_x():
    x = "I am local variable"
    print(x)  # refers local variable for printing it.


read_x()
print(x)  # refers global variable for printing it.
