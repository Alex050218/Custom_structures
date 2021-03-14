from DinArray import DinamicArray


def status_array(ar):
    if not isinstance(ar, DinamicArray):
        raise TypeError("Not a dinamic array")

    print(
        f"""
    New array: {ar.get_string()}
    New capacity: {ar.capacity()}
    New lenght: {ar.get_len()} \n"""
    )


array = DinamicArray(capacity=5, data_type=bool)

print(
    f"""\
Created array of capacity {array.capacity()}

Data type {array.get_type()}

is it Empty? {"Yes" if array.is_empty() else "No"}"""
)

array.set_at(4, True)
print(
    f"""
New value 'True' at index 4

Amount of values introduced into the array by the user: {array.get_len()}

String of the created array: {array.get_string()}

Iteration of all values in the array:"""
)

for val in iter(array):
    print(f"\t {val}")

print("Representation of the array :", array)

print(
    f"""
is within the array a true value?: {'Yes' if array.contains(True) else 'No'}

The index of true is: {array.index_of(True)}

Removing true from the array..."""
)

array.remove_at(4)
status_array(array)

print("Removing the first instance of 'None'...")
array.remove(None)
status_array(array)

print("Adding a false value to the array to an existing empty array")
array.add_val(False)
status_array(array)

full_array = DinamicArray(capacity=3, data_type=bool)

for _ in range(full_array.capacity()):
    full_array.add_val(True)

print("Array before adding new value")
status_array(full_array)

full_array.add_val(False)
print("Array after the new value being inserted")
status_array(full_array)

array.clear()
print("All values deleted from the array and size set to its respective default value")
