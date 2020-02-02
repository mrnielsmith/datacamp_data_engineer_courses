from .parent_class import ParentClass

class SuperChild(ParentClass):
    def __init__(self):
        super().__init__()
        print('super')
