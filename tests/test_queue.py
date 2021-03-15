from Structures.LList import Node


class Queue:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._length = 0

    def enque(self, new_node: Node):
        if self._head is None:
            self._head = new_node
            self._tail = new_node

        new_node.next = self._tail
        self._tail = new_node
