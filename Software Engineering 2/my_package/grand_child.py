from .super_child import SuperChild

class GrandChild(SuperChild):
    def __init__(self):
        super().__init__()
        print('grandchild')
