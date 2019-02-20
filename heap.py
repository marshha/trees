#!/usr/bin/python3

def heap_parent_idx(child_idx):
    if child_idx == 0:
        return None

    return int((child_idx - 1) / 2)

def heap_lchild_idx(parent_idx):
    return int(2*parent_idx)+1

def heap_rchild_idx(parent_idx):
    return int(2*parent_idx)+2

class MinHeap(object):
    def __init__(self):
        self._heap = []

    def getMin(self):
        if self._heap:
            return self._heap[0]

        return None

    def extractMin(self):
        min_val = self.getMin()
        self.delete(min_val)
        return min_val

    def _swap(self, idx1, idx2):
        tmp_val = self._heap[idx1]
        self._heap[idx1] = self._heap[idx2]
        self._heap[idx2] = tmp_val

    def insert(self, val):
        curr_idx = len(self._heap)
        self._heap.append(val)

        # do the bubble-up/sift-up operation - check if parent
        # is greater, if so, then swap
        parent_idx = heap_parent_idx(curr_idx)
        while parent_idx is not None and self._heap[curr_idx] < self._heap[parent_idx]:
            self._swap(curr_idx, parent_idx)

            # move up the heap tree and test again
            curr_idx = parent_idx
            parent_idx = heap_parent_idx(curr_idx)

    def _find_idx(self, val):
        for i in range(0, len(self._heap)):
            if val == self._heap[i]:
                return i

        return None

    def _min_child(self, parent_idx):
        lchild_idx = heap_lchild_idx(parent_idx)
        rchild_idx = heap_rchild_idx(parent_idx)

        lchild_val = self._heap[lchild_idx] if lchild_idx < len(self._heap) else None
        rchild_val = self._heap[rchild_idx] if rchild_idx < len(self._heap) else None

        if lchild_val is None and rchild_val is None:
            return None
        elif lchild_val is not None and rchild_val is None:
            return lchild_idx
        elif rchild_val is not None and lchild_val is None:
            return rchild_idx

        # both children exist
        min_val = min(lchild_val, rchild_val)
        if min_val == lchild_val:
            return lchild_idx

        return rchild_idx

    def delete(self, val):
        curr_idx = self._find_idx(val)
        if curr_idx is None:
            return

        # swap the right-most node into this position
        # (right-most meaning the last node in the list)
        swap_idx = len(self._heap) - 1
        self._swap(curr_idx, swap_idx)
        self._heap.pop()

        if swap_idx == curr_idx:
            return

        # now sift up/down based on the comparison
        # get the parent node's value - if it is
        # greater than current value, sift up,
        # otherwise sift down
        parent_idx = heap_parent_idx(curr_idx)
        if parent_idx is not None and self._heap[parent_idx] > self._heap[curr_idx]:
            while parent_idx is not None:
                if self._heap[parent_idx] > self._heap[curr_idx]:
                    self._swap(parent_idx, curr_idx)
                else:
                    break

                curr_idx = parent_idx
                parent_idx = heap_parent_idx(curr_idx)
        else:
            # parent is less than child or parent doesn't exist, sift down
            child_idx = self._min_child(curr_idx)
            while child_idx is not None:
                if self._heap[child_idx] < self._heap[curr_idx]:
                    self._swap(child_idx, curr_idx)
                else:
                    break

                curr_idx = child_idx
                child_idx = self._min_child(curr_idx)
