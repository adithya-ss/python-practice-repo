# Same name, same arguments.
# Python supports method overriding, but the methods should be different classes.

class Parent:
    def __init__(self):
        pass

    def print_class_name(self, clsName):
        print("Printing from " + clsName + " class.")

class ChildA(Parent):
    def __init__(self):
        pass

    def print_class_name(self, clsName):
        print("Printing from " + clsName + " class.")

class ChildB(ChildA):
    def __init__(self):
        pass

    def print_class_name(self, clsName):
        print("Printing from " + clsName + " class.")


par_obj = Parent()
par_obj.print_class_name(type(par_obj).__name__)

ch_a_obj = ChildA()
ch_a_obj.print_class_name(type(ch_a_obj).__name__)

ch_b_obj = ChildB()
ch_b_obj.print_class_name(type(ch_b_obj).__name__)