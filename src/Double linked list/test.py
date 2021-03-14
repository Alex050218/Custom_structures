from DlList import DNode, DoLList

Llist = DoLList()

for val in range(10):
    Llist.At_beggining(DNode(val))

print(f"New Double Linked List: {Llist.get_str()} \n")

Llist.At_end(DNode(-1))
print(f"New value at end of the list: {Llist} \n")

Llist.insert_at(0, DNode(-2))
print(f"New value at index 0: {Llist} \n")

search_index = 8
Llist.insert_at(search_index, DNode(-3))
print(f"New value at index {search_index}: {Llist} \n")

data = 8
Node = DNode(data)
print(f"Index of first instance of {data}: {Llist.get_index(Node)} \n")

index = 9
print(f"Value at index {index}: {Llist.get_at(index)} \n")

print(f"Current lenght of the list: {Llist.get_lenght()} \n")

Llist.del_first()
print(f"First value deleted: {Llist} \n")

del_index = 7
Llist.del_at(del_index)
print(f"Deleted value at index {del_index}: {Llist} \n")

del_data = 8
deleted = Llist.del_instance(DNode(del_data))

if deleted:
    print(f"Deleted first instance of {del_data}: {Llist} \n")
else:
    print(f"The value {del_data} was not found in the list \n")

print("Iterating trough the list:")
iter_list = iter(Llist)

first_val = next(iter_list)
print(f"Next value: {first_val.data}")

second_val = next(iter_list)
print(f"Second value: {second_val.data}")
