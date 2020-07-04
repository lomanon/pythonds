

class Queue():
    """Define a standard queue class"""

    def __init__(self):
        self.items = []

    def is_empty(self):
        if(len(self.items)) == 0:
            return True
        else:
            return False

    def enqueue(self,item):
        self.items.insert(0,item)

    def size(self):
        return len(self.items)

    def dequeue(self):
        return self.items.pop()

    def items(self):
        return self.items

