#!/usr/bin/python3

class BSTNode(object):
    def __init__(self, val):
        self.val = val
        self.count = 1
        self.left = None
        self.right = None
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
                    break
            else:
                if parent.left:
                    parent = parent.left
                else:
                    parent.left = new_node
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
