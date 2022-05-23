# Same name, differnt arguments.
# Python does not inherently support method overloading
# The only way something similar to overloading can be acheived is by enabling conditional checks for parameters
# to be NULL or NOT NULL inside a method. This is just a trick, but the method will always be one. We can not have
# 2 methods with same name but different arguments in python.

class Parent:
    def __init__(self):
        pass

    def add_nums(self, num1=None, num2=None, num3=None):
        if num1 != None and num2 != None and num3 != None:
            return num1 + num2 + num3
        elif num1 != None and num2 != None:
            return num1 + num2
        else:
            return num1

    
obj1 = Parent()
print(obj1.add_nums(10,20))
print(obj1.add_nums(10,20,30))
print(obj1.add_nums(10))
print(obj1.add_nums())

