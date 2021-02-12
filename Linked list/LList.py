class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    _lenght = 1
    _head = None

    def __init__(self, firstNode):
        self._check_node(firstNode)
        self._head = firstNode

    def AtBeggining(self, NewNode):
        self._check_node(NewNode)
        self._lenght += 1

        NewNode.next = self._head
        self._head = NewNode

    def AtEnd(self, NewNode):
        self._check_node(NewNode)
        self._lenght += 1

        curr_node = self._head
        while curr_node is not None:
            if curr_node.next is None:
                curr_node.next = NewNode
                break
            curr_node = curr_node.next

    def Lenght(self):
        return self._lenght

    def getString(self):
        string = ""

        cur_node = self._head
        while cur_node is not None:
            if cur_node.next is not None:
                string += f"{cur_node.data} -> "
            else:
                string += f"{cur_node.data}"

            cur_node = cur_node.next

        return string

    def __repr__(self):
        return self.getString()

    def _check_node(self, node):
        if not isinstance(node, Node):
            raise ValueError("The introduced value is not a node")
