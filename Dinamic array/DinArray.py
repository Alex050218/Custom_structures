class DinArray:
    _array = []
    _data_type = None
    _capacity = 0
    _len = 0

    def __init__(self, capacity, data_type):
        if capacity < 0:
            raise ValueError("Capacity must be 0 or more")

        if not isinstance(data_type, object):
            raise TypeError("Data type must be an object")

        self._data_type = data_type
        self._capacity = capacity

        for _ in range(capacity):
            self._array.append(None)

    def capacity(self):
        return self._capacity

    def get_len(self):
        return self._len

    def is_empty(self):
        return self.get_len() == 0

    def get(self, index):
        return self._array[index]

    def set_at(self, index, val):
        if not isinstance(val, self._data_type):
            raise ValueError(f"Data type of {val} different to array")

        if self._array[index] is None:
            self._len += 1

        self._array[index] = val

    def get_type(self):
        return self._data_type

    def clear(self):
        self._array = []
        for _ in range(self.capacity()):
            self._array.append(None)

        self._len = 0
