#!/usr/bin/python3

class BSTNode(object):
    def __init__(self, val):
        self.val = val
        self.count = 1
        self.left = None
        self.right = None
        self.parent = None
        return

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = BSTNode(val)
        if not self.root:
            self.root = new_node
            return

        parent = self.root
        while parent:
            if val == parent.val:
                parent.count += 1
                break
            elif val > parent.val:
                if parent.right:
                    parent = parent.right
                else:
                    parent.right = new_node
                    new_node.parent = parent
                    break
            else:
                if parent.left:
                    parent = parent.left
                else:
                    parent.left = new_node
                    new_node.parent = parent
                    break

        return

    def delete(self, val):
        return

    def _list(self, node):
        my_list = []

        if node:
            for x in range(0, node.count):
                my_list.append(node.val)

            if node.left:
                my_list = self._list(node.left) + my_list

            if node.right:
                my_list = my_list + self._list(node.right)

        return my_list

    def get_list(self):
        return self._list(self.root)

    def _iter_node(self, node):
        if node:
            if node.left:
                yield from self._iter_node(node.left)

            yield node

            if node.right:
                yield from self._iter_node(node.right)

    def _iter(self, node):
        if node:
            if node.left:
                yield from self._iter(node.left)

            for x in range(0, node.count):
                yield node.val

            if node.right:
                yield from self._iter(node.right)

    def iter(self):
        yield from self._iter(self.root)

    def _next(self, node):
        if node.right:
            return next(self._iter_node(node.right))

        while node:
            if node.parent == None:
                return None

            if node == node.parent.left:
                return node.parent

            node = node.parent

        return node

    def next(self, val):
        curr_node = self._find_node(val)
        if not curr_node:
            return None

        next_node = self._next(curr_node)
        if next_node:
            return next_node.val

        return None

    def _prev(self, node):
        if node.left:
            # walk to the right-most node from the left branch
            node = node.left
            while node:
                if node.right:
                    node = node.right
                else:
                    return node

        while node:
            if node.parent == None:
                return None

            # Take all the left branches back up the tree
            # until it reaches a value on the right branch
            # of the parent node - this is the first value
            # the input node was greater than.
            if node.parent.right == node:
                return node.parent

            node = node.parent

        return None

    def prev(self, val):
        curr_node = self._find_node(val)
        if not curr_node:
            return None

        prev_node = self._prev(curr_node)
        if prev_node:
            return prev_node.val

        return None

    def _find_node(self, val):
        found_node = None

        parent = self.root
        while parent:
            if val == parent.val:
                found_node = parent
                break
            elif val > parent.val:
                if parent.right:
                    parent = parent.right
                else:
                    break
            else:
                if parent.left:
                    parent = parent.left
                else:
                    break

        return found_node

    def find(self, val):
        return self._find_node(val) != None
