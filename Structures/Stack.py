from __future__ import annotations
from Structures.LList import LinkList, Node

b = 2

class StackS(LinkList):
    def __init__(self, new_head: Node | None = None):
        super().__init__(new_head=new_head)

        if new_head is not None:
            self._head = new_head
        else:
            self._head = Node()
