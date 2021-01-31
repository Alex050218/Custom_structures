from DinArray import DinArray

array = DinArray(capacity=5, data_type=bool)
print(f"Created array of capacity {array.size()}")

print(f"\n is it Empty? {array.isEmpty()}")

print(f"\n Value at index 4: {array.get(4)}")

array.set(True, 0)
print("\n New value 'True' at index 0")
