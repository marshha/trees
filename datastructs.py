#!/usr/bin/python3

'''
Last in, first out
'''
class Stack(object):
    def __init__(self):
        self._stack = []
        return

    def push(self, val):
        self._stack.append(val)
        return

    def pop(self):
        return self._stack.pop()

'''
First in, first out
'''
class Queue(object):
    def __init__(self):
        self._queue = []
        return

    def push(self, val):
        self._queue.append(val)
        return

    def pop(self):
        return self._queue.pop(0)
