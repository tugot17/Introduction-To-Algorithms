class Element:
    def __init__(self, value, previous):
        self.value = value
        self.previous = previous

class EmptyStackException(Exception):
    pass


class Stack(object):
    head = None


    def isEmpty(self):
        return self.head == None

    def push(self, value):
        self.head = Element(value, self.head)

    def peek(self):
        if(self.isEmpty()):
            raise EmptyStackException
        return self.head.value

    def pop(self):
        if(self.isEmpty()):
            raise EmptyStackException

        returned_element = self.head.value
        self.head = self.head.previous

        return returned_element




