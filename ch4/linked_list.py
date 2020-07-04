# Implement a linked list as a first step towards making an unordered list

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,data_item):
        self.data = data_item

    def setNext(self,next_item):
        self.next = next_item

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        item_node = Node(item)
        item_node.setNext(self.head)
        self.head = item_node

    def size(self):
        count = 0

        item = self.head
        while True:
            if item == None:
                break
            else:
                count +=1
                item = item.getNext()
        return count

    def find(self,item):
        list_item = self.head

        index = 0
        found = False
        while list_item != None:
            if list_item.getData() == item:
                found = True
                return index
            else:
                list_item = list_item.getNext()
                index +=1

        if found:
            return index

    def get_items(self):
        item = self.head

        while item is not None:
            print(item.getData())
            item = item.getNext()

    def remove(self,item):
        current = self.head
        previous = None

        while current is not None:

            # Check item and remove
            if item == current.getData():
                if previous is not None:
                    previous.setNext(current.getNext())
                else:
                    self.head = current.getNext()

            # Increment references
            previous = current
            current = current.getNext()


    def append(self,item):
        list_item = self.head
        item_node = Node(item)

        if list_item == None:
            self.head = item_node
            return

        while list_item.getNext() is not None:
            list_item = list_item.getNext()

        list_item.setNext(item_node)


def main():
    s = UnorderedList()
    s.append(2)
    s.get_items()

if __name__ == "__main__":
    main()