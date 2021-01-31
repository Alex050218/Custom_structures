class DinArray:
    _array = []
    _capacity = 0
    _data_type = None

    def __init__(self, capacity, data_type):
        if capacity <= 0:
            raise ValueError("Capacity must be 1 or more")

        self._data_type = data_type
        self._capacity = capacity

        for _ in range(capacity):
            self._array.append(None)

    def size(self):
        return self._capacity

    def isEmpty(self):
        return self._capacity == 0

    def get(self, index):
        return self._array[index]

    def set(self, val, index):
        if isinstance(val, self._data_type):
            self._array[index] = val
        else:
            raise TypeError(f"Data type of {val} different to array")

    def getType(self):
        return self._data_type

    def clear(self):
        curr_ind = 0
        while curr_ind < self._capacity:
            self._array[curr_ind] = None
            curr_ind += 1
