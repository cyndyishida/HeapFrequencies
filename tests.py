from string import ascii_lowercase
import Heap

def test_most_x():
    result = Heap.most_x_common(['a','a','a','b','b','c'], 2)
    assert result == set('ab')

    result = Heap.most_x_common(['a','a','a','b','b','b','c'], 3)
    assert result == set('abc')

    result = Heap.most_x_common(list('a'* 99 + 'b'), 1)
    assert result == {'a'}



def test_most_x_h():
    result = Heap.most_x_common(['z', 'a', 'b', 'a'],1)
    assert result == {'a'}

    result = Heap.most_x_common(['z', 'a', 'o'],1)
    assert result == {'z'}

    result = Heap.most_x_common(['z', 'a', 'o'],3)
    assert result == set('zao')

    result = Heap.most_x_common(['a','a','a','b','b','c','d','d','z'], 4)
    assert result == set('abdz')

def test_most_x_h1():
    result = Heap.most_x_common(list('abb'* 9999),1)
    assert result == {'b'}
    result = Heap.most_x_common(list('abc'* 9999 + 'c'),1)
    assert result == {'c'}
    result = Heap.most_x_common(list('abcz'* 9999 + 'cz'*999),3)
    assert result == set('czb')
    result = Heap.most_x_common(list(ascii_lowercase * 9999), 26)
    assert result == set(ascii_lowercase)


def underlying_data_check(heap):
    # simple validator that the underlying contigious data has the accurate ordering

    for i in range(0, (heap._size -1) // 2 ):
        assert heap._data[i] < heap._data[i *2 + 1]
        if i * 2 +2  < heap._size:
            assert heap._data[i] < heap._data[i * 2 + 2]

def test_push():

    heap = Heap.Heap(10)
    heap.push(5, 'c')
    heap.push(4, 'y')
    heap.push(3, 'n')
    heap.push(2, 'd')
    heap.push(5, 'y')

    assert heap._size == 5
    assert heap.top() == 'd'
    underlying_data_check(heap)

    heap = Heap.Heap(2)
    heap.push(5, 'c')
    heap.push(4, 'y')
    heap.push(3, 'n')

    assert heap._size == 2
    assert heap.top() == 'y'
    assert [i.get_val() for i in heap._data if i] == ['y', 'c']


def test_push_h():
    heap = Heap.Heap(25)
    for i in ascii_lowercase:
        heap.push(key=1, val=i)
    assert heap._size == 25
    assert heap.top() == 'b'
    underlying_data_check(heap)

    heap = Heap.Heap(26)
    for i,ch in enumerate(ascii_lowercase):
        heap.push(key=i, val=ch)
        heap.push(key=1, val=ch)
    assert heap._size == 26
    assert heap.top() == 'y'
    underlying_data_check(heap)

def test_pop():
    heap = Heap.Heap(10)
    heap.push(5, 'c')
    heap.push(4, 'y')
    heap.push(3, 'n')
    heap.push(2, 'd')
    heap.push(5, 'y')

    assert heap._size == 5
    assert heap.top() == 'd'
    for i in range(heap._size):
        assert heap.top() == heap.pop()
    assert i == 4
    assert heap.is_empty()

    heap = Heap.Heap(2)
    heap.push(5, 'c')
    heap.push(4, 'y')
    heap.push(3, 'n')

    assert heap._size == 2
    assert heap.pop() == 'y'
    assert heap.pop() == 'c'
    assert heap.is_empty()

def test_pop_h():
    heap = Heap.Heap(25)
    for i in ascii_lowercase:
        heap.push(key=1, val=i)
    assert heap._size == 25
    for i in range(heap._size - 5):
        assert heap.top() == heap.pop()
    assert not heap.is_empty()
    assert heap._size == 5

    heap = Heap.Heap(26)
    for i,ch in enumerate(ascii_lowercase):
        heap.push(key=i, val=ch)
        heap.push(key=1, val=ch)

    underlying_data_check(heap)
    for i in range(heap._size):
        assert heap.top() == heap.pop()
    assert heap.is_empty()
    assert heap._size == 0
    assert heap.top() is None

def test_min_child():
    pass
