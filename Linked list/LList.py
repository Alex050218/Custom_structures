class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    _lenght = 1
    _head = None
    _tail = None

    def __init__(self, firstNode):
        self._check_node(firstNode)
        self._head = firstNode

    def _check_node(self, node):
        if not isinstance(node, Node):
            raise ValueError("The introduced value is not a node")
