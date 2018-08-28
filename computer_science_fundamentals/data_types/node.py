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

    def create_child_nodes(self, child_node_values, is_doubly_linked=False):
        """
        Create individual child nodes with child_node_values.

        :param list child_node_values: values to create child nodes for
        :param bool is_doubly_linked: self will be doubly linked to child if True
        """
        for value in child_node_values:
            self.children[value] = Node(value)
            if is_doubly_linked:
                child = self.children[value]
                child.parents[self.value] = self

    def create_parent_nodes(self, parent_node_values, is_doubly_linked=False):
        """
        Create individual parent nodes with parent_node_values.

        :param list parent_node_values: values to create parent nodes for
        :param bool is_doubly_linked: self will be doubly linked to parent if True
        """
        for value in parent_node_values:
            parent = Node(value)
            parent.children[self.value] = self
            if is_doubly_linked:
                self.parents[parent.value] = parent
