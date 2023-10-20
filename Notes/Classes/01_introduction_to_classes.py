class Person:
    """ A simple Class"""                   # docstring
    species = "Home Sapiens"                # Class Attribute

    def __init__(self, name):               # special method
        self.name = name

    def __str__(self):
        """
        This method is run when Python tries to cast the object to a string. print statement.
        :return:
        """
        return self.name

    def rename(self, rename):               # regular method
        self.name = rename
        print("Now Name is {}".format(self.name))