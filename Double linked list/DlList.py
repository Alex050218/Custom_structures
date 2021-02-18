class DNode:
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None


class DoLList:
    def __init__(self):
        self._lenght = 0
        self._head = None

    def _check_DNode(self, new_node):
        if not isinstance(new_node, DNode):
            raise TypeError
