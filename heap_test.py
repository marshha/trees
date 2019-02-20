#!/usr/bin/python3
import random
import heap

minheap = heap.MinHeap()
vals = [ x for x in range(0, 100) ]
random.shuffle(vals)

for v in vals:
    minheap.insert(v)

for x in range(0, int(len(vals)/2)):
    rand_idx = random.randrange(0, len(vals))
    minheap.delete(vals[rand_idx])
    del vals[rand_idx]

heap_list = []
min_val = minheap.extractMin()
while min_val is not None:
    heap_list.append(min_val)
    min_val = minheap.extractMin()

print(heap_list == sorted(vals))
