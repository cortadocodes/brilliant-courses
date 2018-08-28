class Node:
    """
    Create a singly- or doubly-linked node that can be the foundation for a linked list.

    :param any value: data for node to store
    :param bool doubly_linked: doubly-linked if True, singly-linked if False
    """
    def __init__(self, value=None, is_doubly_linked=False):
        self.value = value
        self.next = None

        if isinstance(is_doubly_linked, bool):
            if is_doubly_linked:
                self.previous = None
                self.type = 'doubly-linked'
            else:
                self.type = 'singly-linked'
        else:
            raise TypeError('is_doubly_linked should be boolean.')

    def __repr__(self):
        representation = '{} Node: {}'.format(self.type, self.value)
        return representation
