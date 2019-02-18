#!/usr/bin/python3
import os
import sys
import random
import binarysearch_list as bsl

# tuple is (test_list, search_val, expected_idx)
TESTS = [
    ([ x for x in range(0,100) ], 50, 50),
    ([ x for x in range(0,100) ], 15, 15),
    ([ x for x in range(0,100) ], 25, 25),
    ([ x for x in range(0,100) ], 85, 85),
    ([ x for x in range(0,100) ], 86, 86),
    ([ x for x in range(0,100) ], 0, 0),
    ([ x for x in range(0,100) ], 1, 1),
    ([ x for x in range(0,100) ], 2, 2),
    ([ x for x in range(0,100) ], 99, 99),
    ([ x for x in range(0,100) ], 98, 98),
    ([ x for x in range(0,100) ], 97, 97),
    ([1,2,3,4,5], 1, 0),
    ([1,2,3,4,5], 2, 1),
    ([1,2,3,4,5], 3, 2),
    ([1,2,3,4,5], 4, 3),
    ([1,2,3,4,5], 5, 4),
]

for (test_list, search_val, expected_idx) in TESTS:
    loop_idx = bsl.search_list(test_list, search_val)
    rec_idx = bsl.search_list_rec(test_list, search_val)
    if loop_idx != expected_idx:
        print("Loop search failed: ", test_list, search_val, expected_idx, "got ", loop_idx)

    if rec_idx != expected_idx:
        print("Rec search failed: ", test_list, search_val, expected_idx, "got ", rec_idx)

MAX_ITERS=1024
MAX_RANGE=1024*1024
test_list = [ x for x in range(0, MAX_RANGE) ]
for i in range(0, MAX_ITERS):
    sys.stdout.write(str(i))
    search_val = random.randrange(0, MAX_RANGE * 1.5)
    expected_idx = search_val if (search_val < MAX_RANGE) else None

    loop_idx = bsl.search_list(test_list, search_val)
    rec_idx = bsl.search_list_rec(test_list, search_val)
    if loop_idx != expected_idx:
        print("Loop search failed: ", test_list, search_val, expected_idx, "got ", loop_idx)

    if rec_idx != expected_idx:
        print("Rec search failed: ", test_list, search_val, expected_idx, "got ", rec_idx)

    sys.stdout.write("\r")

