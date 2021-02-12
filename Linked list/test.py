from LList import LinkList, Node

Llist = LinkList(Node(5))

for val in range(1, 10, 2):
    Llist.AtBeggining(Node(val))

Llist.AtEnd(Node(9))
