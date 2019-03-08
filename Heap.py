class Node:
    """
    Class definition shouldn't be modified in anyway
    """
    __slots__ = '_key', '_val'

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
        return '(k: {0} v: {1})'.format(str(self._key), str(self._val))

    __repr__ = __str__

    def __hash__(self):
        return hash(str(self))

    @property
    def val(self):
        """
        :return: getter
        """
        return self._val


class Heap:
    """
    Class definition is partially completed.
    Function signatures and provided functions may not be edited in anyway.
    """
    __slots__ = '_size', '_capacity', '_data'

    def __init__(self, capacity):
        self._size = 0
        self._capacity = capacity + 1  # additional element space for push
        self._data = [None] * self._capacity

    def __str__(self):
        return ', '.join(str(el) for el in self._data if el is not None)

    __repr__ = __str__

    """
    DO NOT MODIFY ABOVE
    Start of Student Modifications
    """

    def _percolate_up(self):
        pass

    def _percolate_down(self):
        pass

    def _min_child(self, i):
        pass

    def push(self, key, val):
        pass
    
    def pop(self):
        pass

    @property  # do not remove
    def empty(self):
        pass

    @property  # do not remove
    def top(self):
        pass 

    @property  # do not remove
    def levels(self):
        pass 


def most_x_common(vals, X):
    pass
