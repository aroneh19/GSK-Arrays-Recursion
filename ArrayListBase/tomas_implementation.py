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
        self.arr = [None] * self.capacity

    # Time complexity: O(n) - linear time in size of list
    def __str__(self):
        return_string = ""
        for i in range(self.size):
            return_string += f"{self.arr[i]}, "
        return return_string.rstrip(", ")

    # Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.capacity_check()
        for i in range(self.size - 1, -1, -1):
            self.arr[i + 1] = self.arr[i]

        self.arr[0] = value
        self.size += 1

    # Time complexity: O(n) - linear time in size of list
    def insert(self, value, index: int):
        self.capacity_check()

        if index < 0 or index > self.capacity:
            raise IndexOutOfBounds()

        for i in range(self.size - 1, index - 1, -1):
            self.arr[i + 1] = self.arr[i]

        self.arr[index] = value
        self.size += 1


    # Time complexity: O(1) - constant time
    def append(self, value):
        self.capacity_check()
        self.arr[self.size] = value
        self.size += 1

    # Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if index < 0 or index > self.capacity:
            raise IndexOutOfBounds()

        self.arr[index] = value

    # Time complexity: O(1) - constant time
    def get_first(self):
        if self.size > 0:
            return self.arr[0]
        else:
            raise Empty

    # Time complexity: O(1) - constant time
    def get_at(self, index):
        if index < 0 or index > self.capacity:
            raise IndexOutOfBounds()
        else:
            return self.arr[index]

    # Time complexity: O(1) - constant time
    def get_last(self):
        if self.size > 0:
            return self.arr[self.size - 1]
        else:
            raise Empty
    # Time complexity: O(n) - linear time in size of list
    def resize(self):
        self.capacity *= 2
        tmp_arr = [0] * self.capacity
        for i in range(self.size):
            tmp_arr[i] = self.arr[i]
        self.arr = tmp_arr

    # Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        if index < 0 or index > self.size:
            raise IndexOutOfBounds()
        else:
            for i in range(index, self.size -1):
                self.arr[i] = self.arr[i + 1]
        self.size -= 1

    # Time complexity: O(1) - constant time
    def clear(self):
        self.arr = [0] * self.size

    # Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        pass

    # Time complexity: O(n) - linear time in size of list
    # Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        pass

    # Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        pass

#Helper Functions

    def capacity_check(self):
        if self.size == self.capacity:
            self.resize()

if __name__ == "__main__":
    arr_lis = ArrayList()
    arr_lis.append(1)
    arr_lis.append(2)
    arr_lis.append(3)
    arr_lis.append(4)
    arr_lis.append(5)
    arr_lis.append(100)
    arr_lis.insert(55,5)
    print(str(arr_lis))
    print(arr_lis.get_last())
    arr_lis.remove_at(6)
    print(str(arr_lis))