class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    _lenght = 0
    _head = None
    _curr_node = None

    def __init__(self, new_head=None):
        if new_head is not None:
            self._check_node(new_head)
            self._head = new_head
            self._lenght += 1

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

    def InsertAt(self, index, NewNode):
        self._check_node(NewNode)
        self._check_index(index)

        if index == 0:
            self.AtBeggining(NewNode)
            return

        curr_node = self._head
        for _ in range(index):
            prev_node = curr_node
            curr_node = curr_node.next

        NewNode.next = curr_node
        prev_node.next = NewNode

        self._lenght += 1

    def removeAt(self, index):
        self._check_index(index)

        if index == 0:
            self.remove_first()
            return

        old_node = self._head
        for _ in range(index):
            prev_node = old_node
            old_node = old_node.next

        if old_node.next is None:
            prev_node.next = None
        else:
            prev_node.next = old_node.next

        self._reduce_lenght()

    def remove_node(self, node):
        self._check_node(node)

        if node.data == self._head.data:
            self.remove_first()
            return

        old_node = self._head
        while old_node is not None:
            prev_node = old_node
            old_node = old_node.next

            if old_node.data == node.data:
                break

        if old_node.next is None:
            prev_node.next = None
        else:
            prev_node.next = old_node.next

        self._reduce_lenght()

    def remove_first(self):
        self._reduce_lenght()
        old_head = self._head
        self._head = old_head.next

        del old_head

    def Lenght(self):
        return self._lenght

    def get_data(self, search_index):
        self._check_index(search_index)

        curr_node = self._head
        for curr_index in range(self.Lenght()):
            if curr_index == search_index:
                return curr_node.data

            curr_node = curr_node.next

    def get_index(self, search_node):
        self._check_node(search_node)

        curr_node = self._head
        for index in range(self.Lenght()):
            if search_node.data == curr_node.data:
                return index

            curr_node = curr_node.next

        return -1

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

    def __iter__(self):
        self._curr_node = self._head
        return self

    def __next__(self):
        if self._curr_node is not None:
            data_node = self._curr_node.data
            self._curr_node = self._curr_node.next
            return data_node
        else:
            raise StopIteration

    def _check_node(self, node):
        if not isinstance(node, Node):
            raise ValueError("The introduced value is not a node")

    def _check_index(self, new_index):
        if not new_index >= 0 or not new_index < self._lenght:
            raise IndexError

    def _reduce_lenght(self):
        if self._lenght != 0:
            self._lenght -= 1
