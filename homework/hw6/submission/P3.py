#!/usr/bin/env python3
# File       : P3.py
# Description: Heap implementation (heap ordered balanced binary tree)
# Copyright 2022 Harvard University. All Rights Reserved.


class MinHeap:
    """Minimum heap implementation based on balanced binary tree structure."""

    def __init__(self, x):
        """
        Initialize and build a heap based on random array x.
        Parameters
        ----------
        x : array-like
            Input array with possibly random values.
        """
        self._heap = x
        self._build_heap()

    def __len__(self):
        return len(self._heap)

    def __str__(self):
        return ' '.join([f'{k}' for k in self._heap])

    def _compare(self, a, b):
        return a < b

    def _siftup(self, child):
        if self.left(child) < self.size and self.compare(self._heap[child],self._heap[self.left(child)]):
            temp_val = self._heap[child]
            self._heap[child] = self._heap[self.left(child)]
            self._heap[self.left(child)] = temp_val
            self._siftup(self.left(child))

    def _siftdown(self, parent):
        if self.right(val) < self.size and self.compare(self._heap[child],self._heap[self.right(child)]):
            temp_val = self._heap[val]
            self._heap[val] = self._heap[self.right(val)]
            self._heap[self.right(val)] = temp_val
            self._siftup(self.right(val))

    def _build_heap(self):
        for val in range((self.size-1)/2,-1,-1):
            self._siftdown(val)

    # public interface
    def push(self, value):
        self.size = self.size + 1
        self._heap.append(key)
        val = self.size - 1
        while val > 0:
            temp_val = self._heap[val]
            self._heap[child] = self._heap[self.left(val)]
            self._heap[self.right(val)] = temp_val
            val = self.parent(val)

    def pop(self):
        temp = self._heap[0]
        self._heap[0]=self._heap[self.size-1]
        self.size-=1
        self._siftdown(0)
        return temp

    def top(self):
        """
        Get the top element from the heap (root of tree).
        Returns
        -------
        value
            The method returns the top element in the heap.
        Raises
        ------
        IndexError
            This method raises an `IndexError` if the heap is empty.
        """
        return self._heap[0]  # return h_1 (raises IndexError if heap is empty)


class MaxHeap(MinHeap):
    def compare(self,a,b):
        return a > b


if __name__ == "__main__":
    # TODO: optional test code
    pass
