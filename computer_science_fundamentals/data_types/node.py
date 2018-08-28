class Node:
    """
    Create a singly- or doubly-linked node that can be the foundation for a linked list or trie.

    :param any value: data for node to store
    :param bool doubly_linked: doubly-linked if True, singly-linked if False
    """
    def __init__(self, value=None, is_doubly_linked=False):
        self.value = value
        self.children = {}
        self.parents = {}
        self.is_doubly_linked = is_doubly_linked

        if not isinstance(is_doubly_linked, bool):
            raise TypeError('is_doubly_linked should be boolean.')

    def __repr__(self):
        if self.is_doubly_linked:
            type = 'Doubly-linked'
        else:
            type = 'Singly-linked'
        representation = '{} Node with {} children'.format(type, self.value, len(self.children))
        return representation

    def connect_child_nodes(self, child_nodes):
        for child in child_nodes:
            self.children[child.value] = child
            if child.is_doubly_linked:
                child.parents[self.value] = self

    def connect_parent_nodes(self, parent_nodes):
        for parent in parent_nodes:
            parent.children[self.value] = self
            if self.is_doubly_linked:
                self.parents[parent.value] = parent
