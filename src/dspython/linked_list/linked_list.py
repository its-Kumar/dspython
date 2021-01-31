'''singly linked list implementation'''

from dspython.linked_list import Node


class LinkedList:
    """
    class to represent a singly linked list.
    """

    def __init__(self, head=None):
        """class to represent a singly linked list.

        Args:\n
            head (Any, optional): pointer to store first node of the list. Defaults to None.
        """
        self.head = head

    # count nodes in linked list
    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def print(self):
        """ Print entire linked list """
        if self.head is None:
            print("List is empty....")
        else:
            current = self.head
            while current is not None:
                print(current.data, end="\t")
                current = current.next

    def insert_at_begining(self, data):
        """Insert data at begining

        Args:
            data (Any): data to be stored
        """
        new_node = Node(data)
        if len(self) == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        """Insert data at the end

        Args:
            data (Any): data to be stored
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insert_at_position(self, pos: int, data):
        """Insert data at the given position

        Args:\n
            pos (int): position
            data (Any): data to be stored
        """
        l = len(self)
        if pos > l or pos < 0:
            print("Insertion is not possible..!!")
            return None
        if pos == 0:
            self.insert_at_begining(data)
        elif pos == l:
            self.insert_at_end(data)
        else:
            new_node = Node(data)
            count = 0
            current = self.head
            while count < pos - 1:
                count += 1
                current = current.next
            new_node.next = current.next
            current.next = new_node

    # Deletion
    def delete_first_node(self):
        '''Deletes the first node'''
        if self.head is None:
            print("Deletion not possible")
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def delete_last_node(self):
        '''Deletes the last node'''
        if self.head is None:
            print("Deletion not possible")
            return None
        current = self.head
        prev = self.head
        while current.next is not None:
            prev = current
            current = current.next
        prev.next = None
        return current.data

    def remove(self, data):
        """remove data from the list

        Args:

            data (Any): data to be removed
        """
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            prev = self.head
            while (current.next is not None) or (current.data != data):
                if current.data == data:
                    prev.next = current.next
                    return current.data
                else:
                    prev = current
                    current = current.next
            print("The Value not present in the list")

    def delete_by_position(self, pos: int):
        """Deletes node at the given position

        Args:

            pos (int): position
        """

        if self.head is None:
            print("List is empty")
        else:
            count = 0
            current = self.head
            prev = self.head
            if pos > len(self) or pos < 0:
                print("The position does not exist. Please enter a valid position")
            else:
                while current.next is not None or count < pos:
                    count += 1
                    if pos == count:
                        prev.next = current.next
                        return current.data
                    else:
                        prev = current
                        current = current.next

    def delete(self):
        """deletes the linked list"""
        self.head = None
