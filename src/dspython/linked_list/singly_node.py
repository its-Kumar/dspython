"""Module to represent singly linked list node"""


class Node:
    """Creates singly linked list node"""

    def __init__(self, data, next=None):
        """Creates singly linked list node

        Args:\n
            data (Any): data to be added
            next (Any, optional): pointer to next node. Defaults to None.
        """
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return f"Singly linked list Node ->[{self.data}]"

    def has_next(self) -> bool:
        """returns true if node has a next node"""
        return self.next is not None
