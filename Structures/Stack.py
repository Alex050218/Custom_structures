from __future__ import annotations
from typing import Any
from Structures.LList import LinkList, Node

b = 2

class StackS(LinkList):
    def __init__(self, new_head: Node | None = None) -> None:
        super().__init__(new_head=new_head)

        if new_head is not None:
            self._head = new_head
        else:
            self._head = Node()

    def push(self, new_node: Node) -> None:
        self.InsertAt(0,new_node)

    def get_top(self) -> Any:
        return self.get_data(0)

    def pop(self) -> Any:
        old_head = self.removeAt(0)
        return old_head
