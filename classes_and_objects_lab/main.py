class MyClass:
    """this is my doc"""

    class_variable = 1

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable


first = MyClass(2)
second = MyClass(3)

print(MyClass.__dict__) # {'__module__': '__main__', ... }
print(first.__dict__)     # { 'instance_variable': 2 }
print(second.__dict__)    # { 'instance_variable': 3 }
