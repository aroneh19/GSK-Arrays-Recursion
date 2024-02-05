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
        for i in range(self.size - 1, -1, -1):
            self.arr[i + 1] = self.arr[i]
        self.add_to_array(0, value)

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index: int):
        self.check_index(index, 1)
        self.resize()
        for i in range(self.size - 1, index - 1, -1):
            self.arr[i + 1] = self.arr[i]
        self.add_to_array(index, value)

    #Time complexity: O(1) - constant time
    def append(self, value):
        self.resize()
        self.add_to_array(self.size, value)

    def add_to_array(self, index, value):
        self.arr[index] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        self.check_index(index)
        self.arr[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self):
        first_value = self.arr[0]
        return first_value

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        self.check_index(index)
        return self.arr[index]

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
        self.check_index(index)
        for i in range(index, self.size -1):
            self.arr[i] = self.arr[i + 1]
        self.size -= 1

    #Time complexity: O(1) - constant time
    def clear(self):
        self.size = 0
        self.capacity = 4
        self.arr = [0] * self.capacity

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        if not self.order_check():
            raise NotOrdered("Array is not ordered")
        index = 0
        for i in range(self.size):
            if self.arr[i] >= value:
                break
            index += 1

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        for i in range(self.size - 1):
            if self.arr[i] <= self.arr[i + 1]:
                validator = True
            else:
                validator = False
                break
        if validator:
            return self.binary_search(self.arr, 0, self.size - 1, value)
        else:
            return self.linear_search(self.arr, value, 0)
    
    def binary_search(self, arr, low, high, value):
        if high >= low:
            mid = (high + low) // 2

            if arr[mid] == value:
                return mid
            elif arr[mid] > value:
                return self.binary_search(arr, low, mid - 1, value)
            else:
                return self.binary_search(arr, mid, high + 1, value)
        return None

    def linear_search(self, my_list, value, index):
        if my_list == []:
            return False
        head = my_list[0]
        tail = my_list[1:]
        if head == value:
            return index
        return self.linear_search(tail, value, index + 1)
        
    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        index = self.find(value)
        self.remove_at(index)

    def check_index(self, index, insert=0):
        if index < 0 or index >= (self.size + insert):
            raise IndexOutOfBounds("Index is out of bounds")
        return True
    
    def order_check(self):
        for i in range(self.size - 1):
            if self.arr[i] > self.arr[i + 1]:
                return False
        return True

if __name__ == "__main__":
    arr_lis = ArrayList()
    arr_lis.prepend(99)
    print(arr_lis.get_last())
    arr_lis.append(27)
    arr_lis.insert(33, 1)
    arr_lis.insert(41, 3)
    print(arr_lis.get_at(4))
    print(str(arr_lis))