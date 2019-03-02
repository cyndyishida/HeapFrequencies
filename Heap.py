
class Node:
    # DO NOT MODIFY THIS CLASS #
    def __init__(self, key, val):
        self._key = key
        self._val = val

    def __lt__(self, other):
        return self._key < other._key or (self._key == other._key and self._val < other._val)

    def __gt__(self, other):
        return self._key > other._key or (self._key == other._key and self._val > other._val)

    def __str__(self):
        return f'(k: {self._key} v: {self._val})'

    def get_val(self):
        return self._val

    __repr__ = __str__


class Heap:
    def __init__(self, capacity):
        # DO NOT MODIFY THIS METHOD #
        self._size = 0
        self._capacity = capacity+1
        self._data = [None] * self._capacity

    def __str__(self):
        return ', '.join(str(el) for el in self._data if el is not None)
    
    __repr__ = __str__

    ######## Start of Student Modifications  
        

    def _percUp(self):
        i = self._size - 1 
        while (i - 1) // 2 >= 0:
            if self._data[i] < self._data[(i-1) // 2]:
                self._data[i], self._data[(i-1) // 2] = self._data[(i-1) //2], self._data[i]
            i = (i - 1) // 2

    def _percDown(self):
        i = 0
        while (i * 2 + 1) < self._size:
            mc = self._minChild(i)
            if self._data[i] > self._data[mc]:
                self._data[mc], self._data[i] = self._data[i], self._data[mc]
            i = mc

    def _minChild(self, i):
        # helper function not enforced on students to write 
        if i * 2 + 2 >= self._size:
            return i * 2 + 1
        return i * 2 + 1  if self._data[i * 2 + 1] < self._data[i * 2 + 2] else  i * 2 + 2

    def push(self, key, val):
        self._data[self._size]= Node(key, val)
        self._size += 1
        self._percUp()
        # number of elements in heap should never exceed K
        if self._size == self._capacity:
            self.pop()

    def pop(self):
        if self.is_empty():
            return None

        popped = self._data[0]
        self._data[0], self._data[self._size -1] = self._data[self._size-1], None
        self._size -= 1
        self._percDown()
        return popped.get_val()

    def is_empty(self):
        return self._size == 0

    def top(self):
        return None if self.is_empty() else self._data[0].get_val()


def most_x_common(vals, x):
    """
    Solution:
    build frequency table for each value - O(N)
    add each element in frequency table to heap - O(Nlog(X))
    * in push anytime you exceed X pop the element to get back to a stable state
    removing all contents from heap until empty(at X) into set - O(Xlog(X))
    
    Full RunTime  = Nlog(X)
    """
    heap = Heap(x)
    freq_table = {}
    for i in vals:
        freq_table[i] = freq_table.get(i, 0) + 1

    for ch,freq in freq_table.items():
        heap.push(key=freq, val=ch)

    return {heap.pop() for i in range(x)}


