from string import ascii_lowercase, ascii_uppercase
from Project6.Heap import Heap, most_x_common, Node

def test_most_x():
    result = most_x_common(['a','a','a','b','b','c'], 2)
    assert result == set('ab')

    result = most_x_common(['a','a','a','b','b','b','c'], 3)
    assert result == set('abc')

    result = most_x_common(list('a'* 99 + 'b'), 1)
    assert result == {'a'}



def test_most_x_h():
    result = most_x_common(['z', 'a', 'b', 'a'],1)
    assert result == {'a'}

    result = most_x_common(['z', 'a', 'o'],1)
    assert result == {'z'}

    result = most_x_common(['z', 'a', 'o'],3)
    assert result == set('zao')

    result = most_x_common(['a','a','a','b','b','c','d','d','z'], 4)
    assert result == set('abdz')

def test_most_x_ch():
    result = most_x_common(list('abb'* 9999),1)
    assert result == {'b'}
    result = most_x_common(list('abc'* 9999 + 'c'),1)
    assert result == {'c'}
    result = most_x_common(['a','a','a','b','b','c','d','d','z', 'Z'], 4)
    assert result == set('abdz')
    result = most_x_common(list('abcz'* 9999 + 'cz'*999),3)
    assert result == set('czb')
    result = most_x_common(list(ascii_lowercase * 9999), 26)
    assert result == set(ascii_lowercase)


def test_push():
    heap = Heap(10)
    heap.push(5, 'c')
    heap.push(4, 'y')
    heap.push(3, 'n')
    heap.push(2, 'd')
    heap.push(5, 'y')

    assert heap._size == 5
    assert heap.top == 'd'
    assert min(heap._data[:5]) == heap._data[0]
    assert heap._data[1] < heap._data[3]
    assert heap._data[1] < heap._data[4]

    heap.push(6, 'y')
    assert heap._data[2] < heap._data[5]

    heap = Heap(2)
    heap.push(5, 'c')
    heap.push(4, 'y')
    heap.push(3, 'n')

    assert heap._size == 2
    assert heap.top == 'y'
    assert [i.val for i in heap._data if i] == ['y', 'c']
    

def check_underlying_data(heap):
    # simple validator that the underlying contiguous data has the accurate ordering
    for i in range(0, (heap._size -1) // 2 ):
        assert heap._data[i] < heap._data[i *2 + 1]
        if i * 2 +2  < heap._size:
            assert heap._data[i] < heap._data[i * 2 + 2]

def test_push_h():
    heap = Heap(25)
    for i in ascii_lowercase:
        heap.push(key=1, val=i)
    assert heap._size == 25
    assert heap.top == 'b'
    check_underlying_data(heap)

    heap = Heap(26)
    for i,ch in enumerate(ascii_lowercase):
        heap.push(key=i, val=ch)
        heap.push(key=1, val=ch)
    assert heap._size == 26
    assert heap.top == 'y'
    check_underlying_data(heap)

def test_pop():
    heap = Heap(10)
    heap.push(5, 'c')
    heap.push(4, 'y')
    heap.push(3, 'n')
    heap.push(2, 'd')
    heap.push(5, 'y')

    assert heap._size == 5
    for i in range(heap._size):
        assert heap.top == heap.pop()
    assert i == 4
    assert heap.empty

    heap = Heap(2)
    heap.push(5, 'c')
    heap.push(4, 'y')
    heap.push(3, 'n')

    assert heap._size == 2
    assert heap.pop() == 'y'
    assert not heap.empty

def test_pop_h():
    heap = Heap(25)
    for i in ascii_lowercase:
        heap.push(key=1, val=i)
    assert heap._size == 25
    assert heap.top == 'b'
    for i in range(heap._size - 5):
        assert heap.top == heap.pop()
    assert not heap.empty
    assert heap.top == 'v'
    assert heap._size == 5

    heap = Heap(26)
    for i,ch in enumerate(ascii_lowercase):
        heap.push(key=i, val=ch)
        heap.push(key=1, val=ch)

    check_underlying_data(heap)
    for i in range(heap._size):
        assert heap.top == heap.pop()
    assert heap.empty
    assert heap._size == 0
    assert heap.top is None


def check_min(heap, idx, lhs=None, rhs=None):
    if not (lhs or rhs):
        min_child = -1
    elif not rhs:
        min_child = lhs
    else:
        min_child = lhs if heap._data[lhs] < heap._data[rhs] else rhs
    assert min_child == heap._min_child(idx)

def test_min_child():
    heap = Heap(10)
    for ch in ascii_lowercase:
        heap.push(ord(ch), ch)
    assert heap._size == 10

    check_min(heap, 0,1,2)
    check_min(heap, 2,5,6)
    check_min(heap, 3,7,8)


def test_min_child_h():
    heap = Heap(10)
    for ch in ascii_lowercase:
        heap.push(ord(ch), ch)
    assert heap._size == 10

    check_min(heap, 0,1,2)
    check_min(heap, 2,5,6)
    check_min(heap, 3,7,8)
    # boundary checks
    check_min(heap, 4, 9)
    check_min(heap, 7)

    # boundary check
    check_min(heap, 4, 9)
    check_min(heap, 7)

def test_levels():
    heap = Heap(6)
    for ch in ascii_lowercase[:6]:
        heap.push(ord(ch), ch)
    answer = [
                [Node(97, 'a')],
                [Node(98, 'b'), Node(99, 'c')],
                [Node(100, 'd'), Node(101, 'e'), Node(102, 'f')]
    ]
    assert heap.levels == answer


    heap.pop()
    answer = [
        [Node(98, 'b')],
        [Node(100, 'd'), Node(99, 'c')],
        [Node(102, 'f'), Node(101, 'e')]
    ]
    assert heap.levels == answer


def test_levels_h():
    # boundary checks
    heap = Heap(7)
    for ch in ascii_lowercase[:7]:
        heap.push(ord(ch), ch)
    answer = [
        [Node(97, 'a')],
        [Node(98, 'b'), Node(99, 'c')],
        [Node(100, 'd'), Node(101, 'e'), Node(102, 'f'), Node(103, 'g')]
    ]
    assert heap.levels == answer


    heap = Heap(8)
    for ch in ascii_lowercase[:8]:
        heap.push(ord(ch), ch)
    answer = [
        [Node(97, 'a')],
        [Node(98, 'b'), Node(99, 'c')],
        [Node(100, 'd'), Node(101, 'e'), Node(102, 'f'), Node(103, 'g')],
        [Node(104, 'h')]
    ]
    assert heap.levels == answer

    # mid operation ordering
    heap = Heap(26)
    for ch in ascii_lowercase[:8]:
        heap.push(ord(ch), ch)
    heap.pop()
    for ch in ascii_lowercase[8:]:
        heap.push(ord(ch), ch)

    answer = [[Node(98, 'b')],
        [Node(100, 'd'), Node(99, 'c')],
        [Node(104, 'h'), Node(101, 'e'), Node(102, 'f'), Node(103, 'g')],
        [Node(105, 'i'), Node(106, 'j'), Node(107, 'k'), Node(108, 'l'), Node(109, 'm'), Node(110, 'n'), Node(111, 'o'), Node(112, 'p')],
        [Node(113, 'q'), Node(114, 'r'), Node(115, 's'), Node(116, 't'), Node(117, 'u'), Node(118, 'v'), Node(119, 'w'), Node(120, 'x'), Node(121, 'y'), Node(122, 'z')]
    ]
    assert heap.levels == answer

def test_ch():
    heap = Heap(100)
    for i in range(50):
        heap.push(i, ascii_lowercase[i%26])
    assert heap._size == 50

    for _ in range(25):
        heap.pop()
        check_underlying_data(heap)
    assert heap._size == 25

    for i in range(50):
        heap.push(i, ascii_uppercase[i%26])
        check_underlying_data(heap)
    assert heap._size == 75

    for i in range((heap._size - 1 ) // 2 ):
        check_min(heap, i, i *2 +1, i * 2 + 2)

    for _ in range(75):
        assert not heap.empty
        assert heap.top == heap.pop()

    assert heap.top is None
    assert heap.empty
