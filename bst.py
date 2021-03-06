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
        node = self._find_node(val)
        if not node:
            raise Exception("doesn't exist!")

        if node.count > 1:
            node.count -= 1
            return

        self._delete(node)
        return

    def _delete(self, node):
        # handle the node removal cases
        # if node is a leaf
        if not node.left and not node.right:
            # detach from parent
            if node.parent:
                if node == node.parent.left:
                    node.parent.left = None
                elif node == node.parent.right:
                    node.parent.right = None
            else:
                # if it's the root node, and it had no child nodes,
                # it was the only node.
                if self.root == node:
                    self.root = None

        # if node has one child
        elif (node.left and not node.right) or (node.right and not node.left):
            single_child = node.left if node.left else node.right
            single_child.parent = node.parent
            if node.parent:
                if node == node.parent.left:
                    node.parent.left = single_child
                elif node == node.parent.right:
                    node.parent.right = single_child
            else:
                # if it's the root node, and it has only one child node
                # then the child becomes the root
                if self.root == node:
                    self.root = single_child

        # promote next in order
        else:
            next_node = self._next(node)

            # copy the node contents - no special check for root node
            # as the node does not move
            node.val = next_node.val
            node.count = next_node.count

            # delete recursively - this node should not have 2 children
            # as it otherwise cannot be the next in-order successor.
            self._delete(next_node)

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
