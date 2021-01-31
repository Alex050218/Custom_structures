from DinArray import DinArray

array = DinArray(capacity=5, data_type=bool)

info = f"""\
Created array of capacity {array.capacity()}
Data type {array.get_type()} \n"""
print(info)

print(f'is it Empty? {"Yes" if array.is_empty() == 0 else "No"}')

array.set(True, 0)
print("New value 'True' at index 0 \n")

array.clear()
print("All values deleted from the array and size set to 0")
