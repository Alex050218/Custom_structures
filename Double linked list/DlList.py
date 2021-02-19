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

    def del_first(self):
        next_val = self._head.next
        delattr(next_val, "prev")

        self._head = next_val
        self._reduce_lenght()

    def del_at(self, index):
        self._check_index(index)

        if index == 0:
            self.del_first()
            return

        del_val = self._head
        for search_index in range(index):
            del_val = del_val.next

        prev_val = del_val.prev
        next_val = del_val.next

        prev_val.next = next_val
        next_val.prev = prev_val
        self._reduce_lenght()

    def del_instance(self, node):
        self._check_DNode(node)

        if node.data == self._head.data:
            self.del_first()
            return

        del_val = self._head
        while del_val is not None:
            if del_val.data == node.data:
                break
            del_val = del_val.next

        if del_val is None:
            return False

        prev_val = del_val.prev
        next_val = del_val.next

        prev_val.next = next_val
        next_val.prev = prev_val
        self._reduce_lenght()

        return True

    def get_at(self, index):
        self._check_index(index)

        curr_val = self._head
        for curr_index in range(self._lenght):
            if curr_index == index:
                return curr_val.data

            curr_val = curr_val.next

    def get_lenght(self):
        return self._lenght

    def get_index(self, node):
        self._check_DNode(node)

        curr_val = self._head
        for search_index in range(self._lenght):
            if node.data == curr_val.data:
                return search_index

            curr_val = curr_val.next

        return -1

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

    def __iter__(self):
        self._curr_node = self._head
        return self

    def __next__(self):
        if self._curr_node is not None:
            return_node = self._curr_node
            self._curr_node = self._curr_node.next
            return return_node
        else:
            self._del_attributes()
            raise StopIteration()

    def __repr__(self):
        return self.get_str()

    def _check_index(self, index):
        if not index >= 0 or not index < self._lenght:
            raise IndexError

    def _check_DNode(self, new_node):
        if not isinstance(new_node, DNode):
            raise TypeError

    def _reduce_lenght(self):
        if self._lenght != 0:
            self._lenght -= 1

    def _del_attributes(self):
        if hasattr(self, "_curr_node"):
            delattr(self, "_curr_node")
