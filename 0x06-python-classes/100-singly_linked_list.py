#!/usr/bin/python3
class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initialize a node with data and next_node.

        Args:
            data: An integer representing the data of the node.
            next_node: A Node object representing the next node in the list.
                      Default value is None.

        Raises:
            TypeError: If data is not an integer.
            TypeError: If next_node is not a Node object or None.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Get the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the list."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """Return a string representation of the list."""
        res = []
        current_node = self.__head
        while current_node is not None:
            res.append(str(current_node.data))
            current_node = current_node.next_node
        return "\n".join(res)

    def sorted_insert(self, value):
        """Insert a new node with the given
        value in the correct sorted position.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current_node = self.__head
            while (current_node.next_node is not None and
                   value > current_node.next_node.data):
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node
