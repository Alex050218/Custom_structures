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

print("Iteration of all values in the array:")
for val in iter(array):
    print(f"\t {val}")

print("Representation of the array :", array, "\n")

print(
    f"is within the array a true value?: {'Yes' if array.contains(True) else 'No'} \n"
)

print(f"The index of true is: {array.index_of(True)} \n")

print("Removing true from the array...")
array.remove_at(4)
print(
    f"""
    New array: {array.get_string()}
    New capacity: {array.capacity()}
    New lenght: {array.get_len()}"""
)

array.clear()
print("All values deleted from the array and size set to its respective default value")
