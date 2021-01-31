'''implementation of Circular linked list'''

from .singly_node import Node


class CircularLinkedList:
    """
    class to represent a circular linked list.
    """

    def __init__(self, head=None):
        """class to represent a circular linked list.

        Args:\n
            head (Any, optional): pointer to store first node of the list. Defaults to None.
        """
        self.head = head

    def __len__(self):
        current = self.head
        if current is None:
            return 0
        count = 1
        current = current.next
        while current != self.head:
            current = current.next
            count += 1
        return count

    def print(self):
        """ Print entire linked list """

        current = self.head
        if current is None:
            print("List is empty")
        else:
            while True:
                print(current.data, end="  ")
                current = current.next
                if current == self.head:
                    break

    def insert_at_begining(self, data):
        """Insert data at begining

        Args:
            data (Any): data to be stored
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            current.next = new_node
            self.head = new_node

    def insert_at_end(self, data):
        """Insert data at the end

        Args:
            data (Any): data to be stored
        """
        new_node = Node(data)
        new_node.next = new_node
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        new_node.next = self.head
        current.next = new_node

    def delete_first_node(self):
        '''Deletes the first node'''

        current = self.head
        if current is None:
            print("List Empty")
            return None
        if self.head.next == self.head:
            self.head = None
            return
        while current.next != self.head:
            current = current.next
        current.next = self.head.next
        self.head = self.head.next

    def delete_last_node(self):
        '''Deletes the last node'''

        if self.head is None:
            print("List is empty")
            return None
        if self.head.next == self.head:
            self.head = None
            return
        current = self.head
        temp = self.head
        while current.next != self.head:
            temp = current
            current = current.next
        temp.next = current.next
