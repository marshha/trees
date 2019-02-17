#!/usr/bin/python3
import random
import bst

NUM_ITERS=100
NUM_ENTRIES=1024

MIN_VAL=0
MAX_VAL=1024*1024

results = {
    True: 0,
    False: 0,
}

for i in range(0, NUM_ITERS):
    bst_obj = bst.BST()
    for x in range(0,NUM_ENTRIES):
        bst_obj.insert(random.randint(MIN_VAL,MAX_VAL))

    final_list = bst_obj.get_list()
    res = (final_list == sorted(final_list))
    results[res] += 1

print(results)
