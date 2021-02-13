from LList import LinkList, Node

Llist = LinkList()

for val in range(1, 10, 2):
    Llist.AtBeggining(Node(val))
Llist.AtEnd(Node(9))

print("New Linked List: ", Llist)

Llist.InsertAt(4, Node(2))
print("Insertion at index 4: ", Llist)
