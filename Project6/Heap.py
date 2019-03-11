"""
Project 6 Solution
Implemented by: Cyndy Ishida
inspired by: https://leetcode.com/problems/top-k-frequent-elements/
"""


class Node:
    """
    Class definition shouldn't be modified in anyway
    """
    __slots__ = ('_key', '_val')

    def __init__(self, key, val):
        self._key = key
        self._val = val

    def __lt__(self, other):
        return self._key < other._key or (self._key == other._key and self._val < other._val)

    def __gt__(self, other):
        return self._key > other._key or (self._key == other._key and self._val > other._val)

    def __eq__(self, other):
        return self._key == other._key and self._val == other._val

    def __str__(self):
        return '(k: {0} v: {1})'.format(self._key, self._val)

    __repr__ = __str__

    @property
    def val(self):
        """
        :return: underlying value of node
        """
        return self._val


class Heap:
    """
    Class definition is partially completed.
    Method signatures and provided methods may not be edited in any way.
    """
    __slots__ = ('_size', '_capacity', '_data')

    def __init__(self, capacity):
        self._size = 0
        self._capacity = capacity + 1  # additional element space for push
        self._data = [None for _ in range(self._capacity)]

    def __str__(self):
        return ', '.join(str(el) for el in self._data if el is not None)

    __repr__ = __str__

    def __len__(self):  # allows for use of len(my_heap_object)
        return self._size

    """
    DO NOT MODIFY ANYTHING ABOVE THIS LINE
    Start of Student Modifications
    """

    def _percolate_up(self):
        i = self._size - 1
        while (i - 1) // 2 >= 0:
            if self._data[i] < self._data[(i - 1) // 2]:
                self._data[i], self._data[(i - 1) // 2] = self._data[(i - 1) // 2], self._data[i]
            i = (i - 1) // 2

    def _percolate_down(self):
        i = 0
        while (i * 2 + 1) < self._size:
            kid = self._min_child(i)
            if self._data[i] > self._data[kid]:
                self._data[kid], self._data[i] = self._data[i], self._data[kid]
            i = kid

    def _min_child(self, i):
        if i * 2 + 1 >= self._size:
            return -1
        if i * 2 + 2 >= self._size:
            return i * 2 + 1
        return i * 2 + 1 if self._data[i * 2 + 1] < self._data[i * 2 + 2] else i * 2 + 2

    def push(self, key, val):
        """
        creates node and adds new element
        :param key: int
        :param val: char
        """
        self._data[self._size] = Node(key, val)
        self._size += 1
        self._percolate_up()
        if self._size == self._capacity:
            self.pop()

    def pop(self):
        """
        removes smallest element i.e. root
        :return:
        """
        if self.empty:
            return None

        popped = self._data[0]
        self._data[0], self._data[self._size - 1] = self._data[self._size - 1], None
        self._size -= 1
        self._percolate_down()
        return popped.val

    @property  # do not remove
    def empty(self):
        """
        checks if empty
        :return: Bool
        """
        return self._size == 0

    @property  # do not remove
    def top(self):
        """
        access root
        :return: Node.val
        """
        return None if self.empty else self._data[0].val

    @property  # do not remove
    def levels(self):
        """
        level order traversal of heap
        :return: List[List[Node]]
        """
        level_order = []
        i, lvl = 0, 0
        while 2 ** lvl <= self._size:
            end = self._size if i + 2 ** lvl > self._size else i + 2 ** lvl  # remove None's at end
            level_order.append(self._data[i:end])
            i += 2 ** lvl
            lvl += 1

        return level_order


def most_x_common(vals, X):
    """
    Solution:
        build frequency table for each value - O(N)
        add each element in frequency table to heap - O(Nlog(X))
        * in push anytime you exceed X pop the element to get back to a stable state
        removing all contents from heap until empty(at X) into set - O(Xlog(X))
        * technically I could just access the underlying data in O(X) but I wont break the contract
    Full RunTime  = O(N log(X))
    """
    heap = Heap(X)
    freq_table = {}
    for i in vals:
        freq_table[i] = freq_table.get(i, 0) + 1

    for char, freq in freq_table.items():
        heap.push(key=freq, val=char)

    return {heap.pop() for _ in range(X)}
