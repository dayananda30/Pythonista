
def Decorator(cls):
    instance_list = [None]
    def inner(*args, **kwargs):
        if instance_list[0] is None:
            instance_list[0] = cls(*args, **kwargs)
        return instance_list[0]
    return inner




@Decorator
class myClass:
    def __init__(self):
        print("Created!!!!")


c1= myClass()
c2= myClass()
c3= myClass()
c4= myClass()
c5= myClass()
c6= myClass()
