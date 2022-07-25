class Node:
    """Class that is a node which connects previous and next nodes if they exist."""
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Queue:
    """Class which is a queue realised with FIFO method."""
    def __init__(self):
        """Constructor which does not take any argument but creates head and tail of queue."""
        self.head = None
        self.tail = None

    def put(self, data):
        """This method allows to put data and make new node - new element of queue."""
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def get(self):
        """This method takes the first element and deletes it from queue."""
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

    def first(self):
        """This method shows the first element of queue."""
        return self.head.data

    def size(self):
        """This method returns size of queue."""
        temp = self.head
        counter = 0
        while temp is not None:
            counter += 1
            temp = temp.next
        return counter

    def isEmpty(self):
        """This method shows is the queue empty or not."""
        return True if self.head else False

    def __str__(self):
        """Method which gives a queue when it is called with 'print()' function."""
        result = ''
        temp = self.head
        if temp == None:
            return "Queue is empty."
        while temp != None:
            result += f'{temp.data} -> '
            temp = temp.next
        return result[:-4]

queue = Queue()
print(queue)
queue.put(10)
print(queue)
queue.put(12)
print(queue)
queue.put(18)
print(queue)
queue.get()
print(queue)

