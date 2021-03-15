from Structures.LList import Node


class Queue:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._length = 0

    def enque(self, new_node: Node):
        self._length += 1
        if self._head is None:
            self._head = new_node
            self._tail = new_node

        self._tail.next = new_node
        self._tail = new_node
