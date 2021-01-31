"""Module to represent doubly linked list node"""


class Node:
    """Creates doubly linked list node"""

    def __init__(self, data, next=None, prev=None):
        """Creates doubly linked list node

        Args:

            data (Any): data to be added
            next (Any, optional): pointer to next node. Defaults to None.
            prev(Any, optional): pointer to previous node. Defaults to None.
        """
        self.prev = prev
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return f"Doubly linked list Node ->[{self.data}]"

    def has_next(self) -> bool:
        """returns true if node has a next node"""
        return self.next is not None

    def has_prev(self) -> bool:
        """returns true if node has a previous node"""
        return self.prev is not None
