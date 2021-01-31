from DinArray import DinArray

array = DinArray(capacity=5, data_type=bool)
print(f"Created array of capacity {array.size()}")

print(f"is it Empty? {array.isEmpty()}")

print(f"Value at index 5 {array.get(4)}")
