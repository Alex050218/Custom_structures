class DinArray:
    _array = []
    _data_type = None
    _capacity = 0
    _len = 0
    _curr_index = 0

    def __init__(self, capacity, data_type):
        if capacity < 0:
            raise ValueError("Capacity must be 0 or more")

        if not isinstance(data_type, object):
            raise TypeError("Data type must be an storable object")

        self._data_type = data_type
        self._capacity = capacity

        for _ in range(capacity):
            self._array.append(None)

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
            self._array.append(None)

        self._len = 0

    def get_string(self):
        if self._len == 0 and self.index_of(None) == -1:
            return "[]"

        str_array = "["
        for index in range(self._capacity - 1):
            str_array += f"{str(self._array[index])}, "

        final_index = index + 1
        str_array += f"{self._array[final_index]}]"

        return str_array

    def contains(self, search_val):
        if not isinstance(search_val, self._data_type):
            raise ValueError(f"Value '{search_val}' is not a primitive data_type")

        for array_val in self._array:
            if array_val == search_val:
                return True

        return False

    def index_of(self, search_obj):
        if not isinstance(search_obj, self._data_type):
            if search_obj is not None:
                raise ValueError(f"'{search_obj}' is not a legal value")

        current_index = 0
        while current_index < self._capacity:
            if self._array[current_index] == search_obj:
                return current_index
            current_index += 1

        return -1

    def remove_at(self, search_index):
        if search_index < 0 or search_index >= self._capacity:
            raise ValueError(f"{search_index} is not an index in the array")

        new_array = []

        curr_index = 0
        while curr_index < self._capacity:
            curr_value = self._array[curr_index]

            if curr_index == search_index:
                self._len -= 1 if self._len != 0 else 0
            else:
                new_array.append(curr_value)

            curr_index += 1

        self._array = new_array
        self._capacity -= 1

    def remove(self, delete_obj):
        delete_index = self.index_of(delete_obj)

        if delete_index == -1:
            return False

        self.remove_at(delete_index)
        return True

    def __repr__(self):
        return self.get_string()

    def __iter__(self):
        self._curr_index = 0
        return self

    def __next__(self):
        if self._curr_index < self._capacity:
            curr_val = self._array[self._curr_index]
            self._curr_index += 1
            return curr_val
        else:
            raise StopIteration
