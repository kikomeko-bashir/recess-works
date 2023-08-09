class ParentClass:
    def parent_method(self):
        print("This is a parent method.")

class ChildClass(ParentClass):
    def child_method(self):
        print("This is a child method.")

obj = ChildClass()
obj.parent_method()  # Output: This is a parent method.
obj.child_method()   # Output: This is a child method.
