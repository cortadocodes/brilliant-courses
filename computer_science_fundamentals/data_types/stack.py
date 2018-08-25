import math


class Stack:
    """
    Implements a high-level demonstration of the stack datatype. Main
    properties:
    * An item can be added to the top of the stack
    * The item at the top of the stack can be popped or peeked at
    * No other element can be accessed
    """

    def __init__(self, max_size=math.inf):
        self.elements = []
        self.max_size = max_size

    def __repr__(self):
        if len(self.elements) > 0:
            representation = 'Stack with top item {}'.format(self.peek())
        else:
            representation = 'Empty stack'
        return representation

    def push(self, item):
        """
        Adds item to the top of the stack.

        :param any item: item to add to top of stack
        """
        if len(self.elements) >= self.max_size:
            raise OverflowError
        self.elements.append(item)

    def pop(self):
        """
        Remove and return the top element of the stack.

        :return any: element at top of stack
        """
        if len(self.elements) == 0:
            raise Exception('Underflow error')
        item = self.elements.pop(-1)
        return item

    def peek(self):
        """
        Return the value of the top element of the stack.

        :return any: element at top of stack
        """
        if len(self.elements) == 0:
            raise Exception('Underflow error')
        item = self.elements[-1]
        return item
