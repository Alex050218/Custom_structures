from DinArray import DinArray

array = DinArray(capacity=5, data_type=bool)

info = f"""\
Created array of capacity {array.size()}
Data type {array.getType()} \n"""
print(info)

values = f"""\
is it Empty? {"Yes" if array.isEmpty() == 0 else "No"}
Value at index 4: {array.get(4)} \n"""
print(values)

array.set(True, 0)
print("New value 'True' at index 0 \n")

array.clear()
print("All values deleted from the array and size set to 0")
