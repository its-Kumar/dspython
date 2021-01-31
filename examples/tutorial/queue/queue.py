if __name__ == "__main__":
    q = Queue()
    q.enQueue("first")
    q.enQueue("second")
    q.enQueue("third")
    q.deQueue()
    print(q.queueFront())
    print(q.queueRear())
