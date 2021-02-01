class DinArray:
    _array = []
    _data_type = None
    _default_val = None
    _capacity = 0
    _len = 0

    def __init__(self, capacity, data_type):
        if capacity < 0:
            raise ValueError("Capacity must be 0 or more")

        if data_type not in [str, bool, float, int]:
            raise TypeError("Data type must be a primitive data type")

        self._data_type = data_type
        self._capacity = capacity

        if data_type in [float, int]:
            self._default_val = 0
        elif data_type is bool:
            self._default_val = False
        else:
            self._default_val = ""

        for _ in range(capacity):
            self._array.append(self._default_val)

    def capacity(self):
        return self._capacity

    def get_len(self):
        return self._len

    def is_empty(self):
        return self._len == 0

    def get(self, index):
        return self._array[index]

    def set_at(self, index, val):
        if not isinstance(val, self._data_type):
            raise ValueError(f"Data type of {val} different to array")

        if val is None:
            raise ValueError("None values can´t be set at array manually")

        if self._array[index] is not val:
            self._len += 1

        self._array[index] = val

    def get_type(self):
        return self._data_type

    def clear(self):
        self._array = []
        for _ in range(self.capacity()):
            self._array.append(self._default_val)

        self._len = 0

    def get_string(self):
        if self._len == 0:
            return "[]"

        str_array = "["
        for index in range(self._capacity - 1):
            str_array += f"{str(self._array[index])}, "

        final_index = index + 1
        str_array += f"{self._array[final_index]}]"
        
        return str_array
