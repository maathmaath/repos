
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        pass

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        pass

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        pass


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.current = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.current

    def next(self):
        """
        :rtype: int
        """
        value = self.current
        self.current = self.iterator.next() if self.iterator.hasNext() else None
        return value

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.current is not None

# Your PeekingIterator object will be instantiated and called as such:


iter = PeekingIterator(Iterator([1, 2, 3, 4, 5]))
while iter.hasNext():
    val = iter.peek()   # Get the next element but not advance the iterator.
    print(val)
    iter.next()         # Should return the same value as [val].
