from ..linked_list import Node


class Queue:
    def __init__(self, data=None):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def queue_rear(self):
        if self.rear is None:
            print("Sorry the queue is Empty")
            raise IndexError
        return self.rear.data

    def queue_front(self):
        if self.front is None:
            print("Sorry the queue is empty")
            raise IndexError
        return self.front.data

    def en_queue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def de_queue(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        temp = self.front
        self.front = temp.next
        self.size -= 1
        if self.front is None:
            self.rear = None
        return temp.data
