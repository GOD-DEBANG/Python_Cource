class Animal:
    name = "Lion"  # Class Attribute

    def __init__(self, age):
        self.age = age  # Instance Attribute

    def show(self):  # Instance Method
        print("How are you")

    @classmethod
    def hello(cls):  # Class Method (targets the class itself)
        print("How are you Brother")

    @staticmethod
    def static():  # Static Method
        print("Hello")


# Object creation (outside class)
obj = Animal(12)

# Calling the static method
obj.static()
