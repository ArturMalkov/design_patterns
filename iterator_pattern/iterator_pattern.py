"""
Iterator is an object that facilitates the traversal of a data structure.
It provides a way to access the elements of an aggregate object sequentially, without exposing its underlying
representation (structure).
It also provides a uniform way to cycle through different collections of objects (lists, dicts, etc.) -
by implementing a common interface allowing us to use all collections polymorphically.

Motivation:
- iteration (traversal) is a core functionality of various data structures
- an iterator is a separate class that facilitates the traversal (separation of concerns):
        - keeps a reference to the current element
        - knows how to move to a different element

The iterator protocol requires:
a) __iter__() to expose the iterator, which uses:
    - __next__() to return each of the iterated elements or
    - raise StopIteration when it's done
"""
# Iterator of a simple binary tree
#   1
#  / \
# 2   3
#
# in-order: 2 1 3 - our scenario
# preorder: 1 2 3
# postorder: 2 3 1


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def __iter__(self):
        return InOrderIterator(self)


class InOrderIterator:  # stateful iterators cannot be recursive (necessary to navigate from current state to next)
    def __init__(self, root):  # + the execution cannot be suspended - you cannot stop during iteration and resume from a particular element
        self.root = self.current = root
        self.yielded_start = False

        while self.current.left:
            self.current = self.current.left

    def __next__(self):
        if not self.yielded_start:
            self.yielded_start = True
            return self.current

        if self.current.right:
            self.current = self.current.right
            while self.current.left:
                self.current = self.current.left
            return self.current
        else:
            p = self.current.parent
            while p and self.current == p.right:
                self.current = p
                p = p.parent
            self.current = p
            if self.current:
                return self.current
            else:
                raise StopIteration


def traverse_in_order(root):
    def traverse(current):
        if current.left:
            for left in traverse(current.left):
                yield left
        yield current
        if current.right:
            for right in traverse(current.right):
                yield right
    for node in traverse(root):
        yield node


if __name__ == '__main__':
    root = Node(1, left=Node(2), right=Node(3))

    iterator = iter(root)
    print([next(iterator).value for x in range(3)])
    # OR
    for x in root:
        print(x.value)

    for y in traverse_in_order(root):
        print(y.value)
