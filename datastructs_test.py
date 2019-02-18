#!/usr/bin/python3
import datastructs

test_vals = [1,2,3,4,5]

stack = datastructs.Stack()
queue = datastructs.Queue()
for val in test_vals:
    stack.push(val)
    queue.push(val)

for x in range(0,len(test_vals)):
    out_val = stack.pop()
    print(out_val)
    if out_val != test_vals[-1 * (x+1)]:
        print("Stack failed")

for x in range(0,len(test_vals)):
    out_val = queue.pop()
    print(out_val)
    if out_val != test_vals[x]:
        print("Queue failed")
