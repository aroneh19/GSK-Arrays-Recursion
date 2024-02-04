class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.arr = [0] * self.capacity

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        return_string = ""
        for i in range(self.size):
            return_string += f"{self.arr[i]}, "
        return return_string.rstrip(", ")

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.resize()
        for i in range(self.capacity - 1, -1, -1):
            self.arr[i + 1] = self.arr[i]
        self.add_to_array(0, value)

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index: int):
        if index < 0 or index > self.capacity:
            raise IndexError("Inde out of bounds")

        self.resize()
        for i in range(self.size):
            if i >= index:
                self.arr[i] = self.arr[i - 1]
        self.add_to_array(index, value)

        # for i in range(self.size):
        #     if i == index:
        #         new_list[i] = value
        #     elif i < index:
        #         new_list[i] = self.arr[i]
        #     else:
        #         new_list[i] = self.arr[i - 1]
        # self.arr = new_list

    #Time complexity: O(1) - constant time
    def append(self, value):
        self.resize()
        self.add_to_array(self.size, value)

    def add_to_array(self, index, value):
        self.arr[index] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_first(self):
        first_value = self.arr[0]
        return first_value

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_last(self):
        last_value = self.arr[self.size - 1]
        return last_value

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        if self.size + 1 > self.capacity:
            self.capacity *= 2
            tmp_arr = [0] * self.capacity

            for i in range(self.size):
                tmp_arr[i] = self.arr[i]
            self.arr = tmp_arr

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def clear(self):
        self.size = 0
        self.capacity = 4
        self.arr = [0] * self.capacity

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

if __name__ == "__main__":
    arr_lis = ArrayList()
    arr_lis.insert(6, 1)
    arr_lis.insert(4, 1)
    print(str(arr_lis))