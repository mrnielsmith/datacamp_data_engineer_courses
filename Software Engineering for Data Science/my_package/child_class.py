from .parent_class import ParentClass

class ChildClass(ParentClass):
    def __init__(self):
        ParentClass.__init__(self)
        print('child')
