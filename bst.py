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

    def _iter(self, node, out_list):
        if node.left:
            self._iter(node.left, out_list)

        for x in range(0, node.count):
            out_list.append(node.val)

        if node.right:
            self._iter(node.right, out_list)

        return

    def get_list(self):
        out_list = []
        if not self.root:
            return out_list

        self._iter(self.root, out_list)

        return out_list

    def find(self, val):
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
        
        if found_node:
            return True

        return False
