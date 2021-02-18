class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoLList:
    def __init__(self):
        self._lenght = 0
        self._head = None

    def At_end(self, node):
        self._check_DNode(node)

        if self._lenght == 0:
            self.At_beggining(node)
            return

        old_lastNode = self._head
        while old_lastNode is not None:
            if old_lastNode.next is None:
                break

            old_lastNode = old_lastNode.next

        node.prev = old_lastNode
        old_lastNode.next = node

        self._lenght += 1

    def At_beggining(self, node):
        self._check_DNode(node)
        self._lenght += 1

        if self._head is None:
            delattr(node, "prev")
            self._head = node
        else:
            setattr(self._head, "prev", node)
            node.next = self._head
            self._head = node

    def insert_at(self, index, node):
        self._check_DNode(node)
        self._check_index(index)

        if index == 0:
            self.At_beggining(node)
            return

        curr_val = self._head
        for _ in range(index - 1):
            curr_val = curr_val.next

        node.prev = curr_val
        node.next = curr_val.next
        curr_val.next = node

        self._lenght += 1

    def get_str(self):
        list_str = ""

        if self._lenght == 0:
            return "<Empty list>"

        curr_val = self._head
        while curr_val is not None:
            if curr_val.next is not None:
                list_str += f"{curr_val.data} <-> "
            else:
                list_str += f"{curr_val.data}"

            curr_val = curr_val.next

        return list_str

    def __repr__(self):
        return self.get_str()

    def _check_index(self, index):
        if not index >= 0 or not index < self._lenght:
            raise IndexError

    def _check_DNode(self, new_node):
        if not isinstance(new_node, DNode):
            raise TypeError