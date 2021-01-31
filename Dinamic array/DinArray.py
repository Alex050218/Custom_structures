class DinArray:
    _array = []
    _data_type = None
    _capacity = 0
    _len = 0

    def __init__(self, capacity, data_type):
        if capacity < 0:
            raise ValueError("Capacity must be 0 or more")

        self._data_type = data_type
        self._capacity = capacity

        for _ in range(capacity):
            self._array.append(None)

    def capacity(self):
        return self._capacity

    def get_len(self):
        real_len = 0
        for val in self._array:
            if val is not None:
                real_len += 1

        return real_len

    def is_empty(self):
        return self.get_len() == 0

    def get(self, index):
        return self._array[index]

    def set_at(self, val, index):
        if isinstance(val, self._data_type):
            self._array[index] = val
        else:
            raise TypeError(f"Data type of {val} different to array")

    def get_type(self):
        return self._data_type

    def clear(self):
        self._array = []
        self._capacity = 0
