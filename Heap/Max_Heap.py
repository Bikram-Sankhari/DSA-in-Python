class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def __str__(self):
        return str(self.heap)

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current_index = len(self.heap) - 1
        parent_index = self._parent(current_index)

        while current_index != 0 and self.heap[parent_index] < value:
            self._swap(current_index, parent_index)
            current_index = parent_index
            parent_index = self._parent(current_index)

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        result = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink(0)

        return result

    def _sink(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if index != max_index:
                self._swap(index, max_index)
                index = max_index
            else:
                return



my_heap = MaxHeap()
my_heap.insert(1)
my_heap.insert(2)
my_heap.insert(3)
my_heap.insert(4)

print(my_heap)