from array_list import Empty

class ArrayList:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.arr = [0] * self.capacity

    def __str__(self):
        ret_string = "current list: "
        for i in range(self.size):
            if i == self.size -1:
                ret_string += f"{self.arr[i]}"
            else:
                ret_string += f"{self.arr[i]}, "
        return ret_string

    def prepend(self, value: int):
        ArrayList.resize(self)
        for i in range(self.size -1, -1, -1):
            self.arr[i + 1] = self.arr[i]
        self.arr[0] = value
        self.size +=1
        return self.arr

    def insert(self, value, index):
        ArrayList.resize(self)
        for i in range(self.size -1, index - 1, -1):
            self.arr[i +1] = self.arr[i]
        self.arr[index] = value
        self.size += 1
        return self.arr

    def append(self, value):
        ArrayList.resize(self)
        self.arr[self.size] = value
        return self.arr

    def set_at(self, value,  index):
        self.arr[index] = value

    def get_first(self):
        ret_val = self.arr[0]
        return ret_val

    def get_at(self, index):
        ret_val = self.arr[index]
        return ret_val

    def get_last(self):
        ret_val = self.arr[self.size -1]
        return ret_val

    def resize(self):
        if self.size == self.capacity:
            self.capacity *= 2
            new_list = [0] * self.capacity

            for i in range(self.size):
                new_list[i] = self.arr[i]
            self.arr = [0] * self.capacity
            self.arr = new_list
        return self.arr

    def remove_at(self, index):
        for i in range(index, self.size -1):
            self.arr[i] = self.arr[i +1]
        self.size -= 1

    def clear(self):
        self.size = 0
        self.capacity = 4
        self.arr = [0] * 4
        return self.arr

a = ArrayList()
a.prepend(2)
a.prepend(3)
a.prepend(5)
a.prepend(6)
a.prepend(2)
a.prepend(9)
a.insert(20, 1)
a.get_first()
a.remove_at(3)
print(a)


