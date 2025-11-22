class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        # Insert at the end
        self.heap.append(value)
        # Fix heap upwards
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        
        # Swap root with last element
        self._swap(0, len(self.heap) - 1)
        max_val = self.heap.pop()
        # Restore heap downward
        self._heapify_down(0)
        
        return max_val

    def peek(self):
        return self.heap[0] if self.heap else None

    # -----------------------------
    # Helper methods
    # -----------------------------
    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self._swap(index, parent)
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == index:
                break

            self._swap(index, largest)
            index = largest

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
