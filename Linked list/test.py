from LList import LinkList, Node

Llist = LinkList()

for val in range(1, 10, 2):
    Llist.AtBeggining(Node(val))
Llist.AtEnd(Node(9))

print("New Linked List: ", Llist)

Llist.InsertAt(4, Node(2))
print("Insertion at index 4: ", Llist)

Llist.removeAt(0)
print("First value deleted: ", Llist)

old_index = 4
Llist.removeAt(old_index)
print(f"Deletion at index {old_index}:", Llist)

search_node = Node(2)
print(f"Index of {search_node.data}: ", Llist.get_index(search_node))
