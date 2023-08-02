#!/usr/bin/python3
"""
Module illustrates use of Node class.
Initializes data and next_node attributes.
Retrieves their values and changes the current value.
to different values.
"""


class Node:
    """ This class defines a node using private instance
    attributes: data and next_node."""
    def __init__(self, data=0, next_node=None):
        """Initializes the private instance attributes: data and next_node."""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = None

    @property
    def data(self):
        """Data Getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """Data Setter"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Next_node Setter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Next_node Setter"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""
Module illustrates the use of SinglyLinkedList class.
Initializes private instance attribute: head.
Retrieves its value and changes it to a different value
Inserts node into correct position in a sorted list.
Prints the list in stdout.
"""


class SinglyLinkedList:
    """This class defines a singly linked list using
    private instance attribute: head."""
    def __init__(self, head=None):
        """Initializes the private instance attribute: head."""
        self.__head = head

    def sorted_insert(self, value):
        """Inserts temp node into correct sorted position."""
        temp = Node(data=value)

        if self.__head is None or self.__head.data >= temp.data:
            temp.next_node = self.__head
            self.__head = temp
        else:
            ptr = self.__head
            while ptr.next_node is not None and ptr.next_node.data < temp.data:
                ptr = ptr.next_node
            temp.next_node = ptr.next_node
            ptr.next_node = temp

    def __repr__(self):
        """Prints the list in stdout."""
        nodes = []
        ptr = self.__head
        while ptr:
            nodes.append(str(ptr.data))
            ptr = ptr.next_node
        return "\n".join(nodes)
