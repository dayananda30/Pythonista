class demo:
    def __init__(self):
        pass

    def demo_method(self):
        print("I am an instance method - I can change instance variable and methoda")

    @classmethod
    def demo_class_method(cls):
        print("I am an a class  method - I can change class variable")

    @staticmethod
    def demo_static_method():
        print("I am a static method, don't have previledge to chnage class or instance variables")