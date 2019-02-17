#!/usr/bin/python3
import random
import bst

NUM_ITERS=100
NUM_ENTRIES=1024

MIN_VAL=0
MAX_VAL=1024*1024

list_results = {
    True: 0,
    False: 0,
}

iter_results = {
    True: 0,
    False: 0,
}

for i in range(0, NUM_ITERS):
    bst_obj = bst.BST()
    for x in range(0,NUM_ENTRIES):
        bst_obj.insert(random.randint(MIN_VAL,MAX_VAL))

    final_list = bst_obj.get_list()

    iter_list = [ val for val in bst_obj.iter() ]

    list_res = (final_list == sorted(final_list))
    iter_res = (iter_list==final_list)

    list_results[list_res] += 1
    iter_results[iter_res] += 1

print(list_results)
print(iter_results)
print(bst.BST().get_list() == [])
