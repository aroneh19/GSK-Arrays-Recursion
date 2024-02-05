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