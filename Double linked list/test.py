from DlList import DNode, DoLList

Llist = DoLList()

for val in range(10):
    Llist.At_beggining(DNode(val))

print(f"New Double Linked List: {Llist.get_str()}")

Llist.At_end(DNode(-1))
print(f"New value at end of the list: {Llist}")
