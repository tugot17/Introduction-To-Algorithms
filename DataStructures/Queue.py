class Element:
    def __init__(self, value):
        self.value = value
        self.next = None
class EmptyQueueException(Exception):
    pass


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None


    def enqueue(self, value):
        new_element = Element(value)

        if (self.head == None) & (self.tail == None):
            self.head = new_element
            self.tail = self.head
        else:
            self.tail.next = new_element
            self.tail = new_element


    def is_empty(self):
        return self.head == None

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueException
        dequed_element = self.head
        self.head = self.head.next

        return dequed_element.value









