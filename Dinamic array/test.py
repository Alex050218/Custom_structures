from DinArray import DinArray

array = DinArray(capacity=5, data_type=bool)
print(f"Created array of capacity {array.size()} \nData type {array.getType()}")

print(f"\n is it Empty? {array.isEmpty()} \n Value at index 4: {array.get(4)}")

array.set(True, 0)
print("\n New value 'True' at index 0")

array.clear()
print("All values set to 'None' or 'Null' for the non-pythonists")
