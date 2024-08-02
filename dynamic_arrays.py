class DynamicArray:
    def __init__(self, initial_capacity=4):
        self.capacity = initial_capacity
        self.length = 0
        self.arr = [None] * self.capacity

    def resize(self):
        new_capacity = 2 * self.capacity
        new_arr = [None] * new_capacity

        for i in range(self.length):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        self.capacity = new_capacity

    def pushback(self, n):
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length += 1

    def __str__(self) -> str:
        return str([self.arr[i] for i in range(self.length)])


if __name__ == "__main__":
    dynamic_array = DynamicArray()
    dynamic_array.pushback(1)
    dynamic_array.pushback(2)
    dynamic_array.pushback(1)
    dynamic_array.pushback(1)
    dynamic_array.pushback(1)
    dynamic_array.pushback(1)
    dynamic_array.pushback(1)
    dynamic_array.pushback(1)
    dynamic_array.pushback(1)
    dynamic_array.pushback(1)
    dynamic_array.pushback(1)
    dynamic_array.pushback(1)
    dynamic_array.pushback(1)
    dynamic_array.pushback(3)

    print(dynamic_array)
