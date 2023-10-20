class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, value):
        self.data = value

    def setNext(self, value):
        self.next = value


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def addNode(self, item):
        new_node = Node(item)
        new_node.setNext(self.head)
        self.head = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.getData())
            current = current.getNext()

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        print(count)
        return count

    def insert(self, position, value):
        if position > self.size() - 1:
            print("Index Out of bounds")
            raise IndexError
        current = self.head
        previous = None
        pos = 0

        if position == 0:
            self.addNode(value)
        else:
            new_node = Node(value)
            while pos < position:
                pos += 1
                previous = current
                current = current.getNext()
            previous.setNext(new_node)
            new_node.setNext(current)

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() is item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        if self.search(item):
            current = self.head
            previous = None
            removed = False
            while current is not None:
                if current.getData is item and previous is None:
                    self.head = current.getNext()
                    return True
                elif current.getData is item:
                    previous.setNext(current.getNext())
                    return True
                else:
                    previous = current
                    current = current.getNext()
            return removed
        else:
            print("No element ")


n = LinkedList()
n.addNode(1)
n.addNode(2)
n.addNode(3)
n.addNode(4)
n.display()
n.size()
n.insert(2,89)
n.display()
n.remove(2)
n.display()

