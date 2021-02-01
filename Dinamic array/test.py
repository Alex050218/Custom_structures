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

print("Iteration of all values in the array: ")
for val in iter(array):
    print(f"\t {val}")

print("\nRepresentation of the array :", array, "\n")

array.clear()
print("All values deleted from the array and size set to its respective default value")
