from DlList import DNode, DoLList

Llist = DoLList()

for val in range(10):
    Llist.At_beggining(DNode(val))

print(f"New Double Linked List: {Llist.get_str()}")

Llist.At_end(DNode(-1))
print(f"New value at end of the list: {Llist}")

Llist.insert_at(0, DNode(-2))
print(f"New value at index 0: {Llist}")

search_index = 8
Llist.insert_at(search_index, DNode(-3))
print(f"New value at index {search_index}: {Llist}")