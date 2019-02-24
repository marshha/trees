#!/usr/bin/python3

class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.terminal = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

    def _insert(self, node, in_str):
        if len(in_str) > 0:
            c = in_str[0]
            if c not in node.children:
                node.children[c] = TrieNode(c)
            self._insert(node.children[c], in_str[1:])

        else:
            node.terminal = True

        return

    def insert(self, in_str):
        self._insert(self.root, in_str)

    def _search(self, node, in_str):
        if len(in_str) > 0:
            c = in_str[0]
            if c not in node.children:
                return False

            return self._search(node.children[c], in_str[1:])

        return node.terminal

    def _searchNode(self, node, in_str):
        if len(in_str) > 0:
            c = in_str[0]
            if c not in node.children:
                return False

            return self._searchNode(node.children[c], in_str[1:])

        return node

    def search(self, in_str):
        return self._search(self.root, in_str)

    def _iterNode(self, node, prefix):
        if node.terminal:
            yield prefix + node.val

        for c in sorted(list(node.children.keys())):
            yield from self._iterNode(node.children[c], prefix + node.val)

        return

    def startsWith(self, in_str):
        start_node = self._searchNode(self.root, in_str)
        yield from self._iterNode(start_node, in_str[:-1])
        return
