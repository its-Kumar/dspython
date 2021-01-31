class Stack:
    """Stack implementation using array implementation.

    Args:
        limit (int): size of the stack
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.stk = []

    def is_empty(self) -> bool:
        """Check for the stcak to be empty
        """
        return self.stk == []

    def is_full(self) -> bool:
        """Check for the stcak to be full
        """
        return len(self) == self.limit

    def __len__(self):
        """return the size of the stack
        """
        return len(self.stk)

    def push(self, item):
        """push operation of stack

        Args:
            item (any): element to insert
        """
        if len(self) >= self.limit:
            print("Stack OverFlow")
            return
        self.stk.append(item)
        # print("Stack after push", self.stk)

    def pop(self):
        """Pop operation of stack

        Returns:
            value at top
        """
        if len(self) <= 0:
            print("Stack Underflow")
            return None
        return self.stk.pop()

    def peek(self):
        """Returns value at top of the stack
        """
        if len(self) <= 0:
            print("Stack Underflow")
            return None
        return self.stk[-1]

    def __repr__(self):
        return f"Stack: {self.stk}"
