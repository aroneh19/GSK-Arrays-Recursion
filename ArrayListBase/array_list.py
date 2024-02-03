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

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        # TODO: remove 'pass' and implement functionality
        return_string = ""
        for i in range(self.size -1):
            return_string += f"{self.arr[i]}, "
        return return_string.rstrip(", ")

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        # TODO: remove 'pass' and implement functionality
        pass



    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index: int):
        self.size += 1
        new_list = [0] * (self.size)

        for i in range(self.size):
            if i == index:
                new_list[i] = value
            elif i < index:
                new_list[i] = self.arr[i]
            else:
                new_list[i] = self.arr[i - 1]
        self.arr = new_list


    #Time complexity: O(1) - constant time
    def append(self, value):
        self.size += 1
        new_list = [0] * (self.size)

        for i in range(self.size):
            if i == self.size - 1:
                new_list[-1] = value
            else:
                new_list[i] = self.arr[i]
        
        self.arr = new_list

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_first(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_last(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
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
        # TODO: remove 'pass' and implement functionality
        pass

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

    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList(6)
    arr_lis.append(6)
    print(str(arr_lis))