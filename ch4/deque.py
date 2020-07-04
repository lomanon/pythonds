# implement the deque class

class Deque():
    def __init__(self):
        self.items = []

    def addFront(self,item):
        self.items.append(4)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

def palchecker(string):

    chardeque =  Deque()

    for character in string:
        chardeque.addRear(character)

    stillEqual = True

    while chardeque.size() >1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()

        if first != last:
            stillEqual = False
        else:
            continue

    return stillEqual

