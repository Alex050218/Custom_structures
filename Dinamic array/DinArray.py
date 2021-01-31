class DinArray:
    _array = []
    capacity = 0
    data_type = None

    def __init__(self, capacity, data_type):
        if capacity <= 0:
            raise ValueError("Capacity must be 1 or more")

        self.data_type = data_type

        for _ in range(capacity):
            self._array.append(None)
