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
