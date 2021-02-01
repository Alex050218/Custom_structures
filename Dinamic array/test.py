from DinArray import DinArray

array = DinArray(capacity=5, data_type=bool)

info = f"""\
Created array of capacity {array.capacity()} \n
Data type {array.get_type()} \n"""
print(info)

print(f'is it Empty? {"Yes" if array.is_empty() else "No"} \n')

array.set_at(4, True)
print("New value 'True' at index 4 \n")

print(f"Amount of values introduced into the array by the user: {array.get_len()}\n")

print(f"String of the created array: {array.get_string()} \n")

array.clear()
print("All values deleted from the array and size set to its respective default value")
