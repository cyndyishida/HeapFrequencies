class Solution:
    class Node:
        def __init__(self, el, count=0):
            self.__data = el
            self.__count = count

        def __lt__(self, other):
            return self.__count < other.__count

        def __gt__(self, other):
            return self.__count > other.__count

        def __eq__(self, other):
            return self.__count == other.__count

        def get_data(self):
            return self.__data

        def __str__(self):
            return f'{self.__data}'

        __repr__ = __str__

    class Heap:
        def __init__(self):
            self._size = 0
            self._data = [Solution.Node(0, 0)]

        def __percUp(self):
            i = self._size
            while i // 2 > 0:
                if self._data[i] > self._data[i // 2]:
                    tmp = self._data[i // 2]
                    self._data[i // 2] = self._data[i]
                    self._data[i] = tmp
                i = i // 2

        def __percDown(self):
            i = 1
            while (i * 2) <= self._size:
                mc = self.maxChild(i)
                if self._data[i] < self._data[mc]:
                    tmp = self._data[i]
                    self._data[i] = self._data[mc]
                    self._data[mc] = tmp
                i = mc

        def maxChild(self, i):
            if i * 2 + 1 > self._size:
                return i * 2
            else:
                if self._data[i * 2] > self._data[i * 2 + 1]:
                    return i * 2
                else:
                    return i * 2 + 1

        def push(self, el):
            self._data.append(el)
            self.__percUp()
            self._size += 1

        def pop(self):
            popped = self._data[1]
            self._data[1] = self._data[self._size]
            self._size = self._size - 1
            self._data.pop()
            self.__percDown()
            return popped

    def most_x_common(self, nums, n):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        heap = self.Heap()
        freq_table = {}
        for i in nums:
            freq_table[i] = freq_table.get(i, 0) + 1

        for k, v in freq_table.items():
            heap.push(Solution.Node(k, v))

        ret = [heap.pop().get_data() for i in range(n)]
        return ret

def main():
    nums = [1,1,1,2, 3, 4, 5,5,6,5,2]
    k = 3
    ret = Solution().topKFrequent(nums, k)

    print(ret)


if __name__ == '__main__':
    main()
    
