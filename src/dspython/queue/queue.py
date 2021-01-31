class Queue:
    """
    Queue Implementation: Circular Queue.
    """

    def __init__(self, limit=5):
        self.front = None
        self.rear = None
        self.limit = limit
        self.size = 0
        self.que = []

    def is_empty(self):
        return self.size <= 0

    def en_queue(self, item):
        if self.size >= self.limit:
            print("Queue Overflow..!!")
            return
        self.que.append(item)
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        self.size += 1
        print("Queue after enQueue:", self.que)

    def de_queue(self):
        if self.size <= 0:
            print("Queue underflow..!!! ")
            return
        self.que.pop(0)
        self.size -= 1
        if self.size == 0:
            self.front = self.rear = None
        else:
            self.rear = self.size - 1
        print("Queue after deQueue: ", self.que)

    def queue_rear(self):
        if self.rear is None:
            print("Sorry the queue is Empty.")
            raise IndexError
        return self.que[self.rear]

    def queue_front(self):
        if self.front is None:
            print("Sorry the queue is Empty.")
            raise IndexError
        return self.que[self.front]
