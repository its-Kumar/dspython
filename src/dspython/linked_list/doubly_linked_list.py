''''Implementation of a doubly linked list'''

from .doubly_node import Node


class DoublyLinkedList:
    '''Class to represent the doubly linked list'''

    def __init__(self, head=None):
        """Class to represent the doubly linked list

        Args:

            head (Any, optional): pointer to the first node. Defaults to None.
        """
        self.head = head

    # Traversal
    def display(self):
        '''print the linked list'''
        ptr = self.head
        if ptr is None:
            print("Link List is empty..")
        else:
            while ptr is not None:
                print(ptr.data, end="  ")
                ptr = ptr.next

    def __len__(self):
        count = 0
        ptr = self.head
        if ptr is None:
            print("Link List is empty..")
        else:
            while ptr is not None:
                count += 1
                ptr = ptr.next
        return count

    # Insertion
    def insert_at_begining(self, data):
        """Insert data at begining

        Args:
            data (Any): data to be stored
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_last(self, data):
        """Insert data at the end

        Args:
            data (Any): data to be stored
        """
        ptr = self.head
        new_node = Node(data)
        if ptr is None:
            self.head = new_node
        else:
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = new_node
            new_node.prev = ptr

    def insert_at_position(self, pos, data):
        """Insert data at the given position

        Args:\n
            pos (int): position
            data (Any): data to be stored
        """
        l = len(self)
        if pos > l or pos < 0:
            print("Invalid position")
            return
        if pos == 0:
            self.insert_at_begining(data)
            return
        if pos == l:
            self.insert_at_last(data)
            return
        ptr = self.head
        count = 0
        new_node = Node(data)
        while count < pos - 1:
            count += 1
            ptr = ptr.next
        new_node.prev = ptr
        new_node.next = ptr.next
        ptr.next = new_node

    def delete_first_node(self):
        '''Deletes the first node'''

        if self.head is None:
            print("List is empty")
            return None
        ptr = self.head
        self.head = ptr.next
        self.head.prev = None
        return ptr.data

    def delete_last_node(self):
        '''Deletes the last node'''

        if self.head is None:
            print("List is empty")
            return None
        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next
        ptr.prev.next = None
        return ptr.data

    def remove(self, data):
        """remove data from the list

        Args:

            data (Any): data to be removed
        """
        if self.head is None:
            print("List is empty")
        else:
            ptr = self.head
            while (ptr.next is not None) or (ptr.data != data):
                if ptr.data == data:
                    ptr.prev.next = ptr.next
                    ptr.next.prev = ptr.prev
                    return ptr.data
                else:
                    ptr = ptr.next
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
            ptr = self.head
            if pos > len(self) or pos < 0:
                print("The position does not exist. Please enter a valid position")
            else:
                while ptr.next is not None or count < pos:
                    count += 1
                    if pos == count:
                        ptr.prev.next = ptr.next
                        ptr.next.prev = ptr.prev
                        return ptr.data
                    else:
                        ptr = ptr.next

    def delete(self):
        """deletes the linked list"""
        self.head = None
