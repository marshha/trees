#!/usr/bin/python3
import random
import sys
import bst

NUM_ITERS=1000
NUM_ENTRIES=2048

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

find_results = {
    True: 0,
    False: 0,
}

next_results = {
    True: 0,
    False: 0,
}

prev_results = {
    True: 0,
    False: 0,
}

for i in range(0, NUM_ITERS):
    sys.stdout.write(str(i))

    bst_obj = bst.BST()
    orig_list = []
    for x in range(0,NUM_ENTRIES):
        orig_list.append(random.randint(MIN_VAL,MAX_VAL))

    for x in orig_list:
        bst_obj.insert(x)

    for x in orig_list:
        if not bst_obj.find(x):
            print("Failed to find ", x)

    # delete half the inserted values - don't delete the root
    # which is a special case
    if random.random() > 0.5:
        for x in range(int(NUM_ENTRIES/2), NUM_ENTRIES):
            bst_obj.delete(orig_list[x])

        orig_list = orig_list[:int(NUM_ENTRIES/2)]
    else:
        for x in range(0, int(NUM_ENTRIES/2)):
            bst_obj.delete(orig_list[x])

        orig_list = orig_list[int(NUM_ENTRIES/2):]

    for x in orig_list:
        if not bst_obj.find(x):
            print("Failed to find after delete", x)

    orig_sorted_nodups = sorted(list(set(orig_list)))

    final_list = bst_obj.get_list()

    iter_list = [ val for val in bst_obj.iter() ]

    list_res = (final_list == sorted(orig_list))
    iter_res = (iter_list == sorted(orig_list))

    rand_idx = random.randrange(0,len(orig_list))
    find_res = bst_obj.find(orig_list[rand_idx])

    rand_idx = random.randrange(0,len(orig_sorted_nodups))
    rand_val = orig_sorted_nodups[rand_idx]
    rand_next_val = orig_sorted_nodups[rand_idx+1] if rand_idx < (len(orig_sorted_nodups) - 1) else None
    rand_prev_val = orig_sorted_nodups[rand_idx-1] if rand_idx > 0 else None

    next_res = (bst_obj.next(rand_val) == rand_next_val)
    if not next_res:
        print("Failed next", bst_obj.next(rand_val), rand_next_val)

    prev_res = (bst_obj.prev(rand_val) == rand_prev_val)
    if not prev_res:
        print("Failed prev", bst_obj.prev(rand_val), rand_prev_val)

    list_results[list_res] += 1
    iter_results[iter_res] += 1
    find_results[find_res] += 1
    next_results[next_res] += 1
    prev_results[prev_res] += 1

    sys.stdout.write("\r")

print("List", list_results)
print("Iter", iter_results)
print("Find", find_results)
print("Next", next_results)
print("Prev", prev_results)
print(bst.BST().get_list() == [])

# specific tests
bst_obj = bst.BST()
for x in [1,2,3,4,5]:
    bst_obj.insert(x)
bst_obj.delete(1)
print (bst_obj.get_list() == [2,3,4,5])

bst_obj = bst.BST()
for x in [1]:
    bst_obj.insert(x)
bst_obj.delete(1)
print (bst_obj.get_list() == [])
