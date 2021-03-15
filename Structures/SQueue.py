from __future__ import annotations
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

    def is_empty(self) -> bool:
        return self._length == 0

    def lenght(self):
        return self._length

    def get_str(self) -> str:
        str_queue: str = ""

        cur_node = self._head
        while cur_node is not None:
            if cur_node.next is None:
                str_queue += f"{cur_node.data}"
            else:
                str_queue += f"{cur_node.data} -> "

            cur_node = cur_node.next

        return str_queue
