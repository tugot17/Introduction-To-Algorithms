class Element:
    def __init__(self, value, previous):
        self.value = value
        self.previous = previous

class EmptyStackException(Exception):
    pass

class Stack(object):
    top = None

    def is_empty(self):
        return self.top == None

    def push(self, value):
        self.top = Element(value, self.top)

    def peek(self):
        if(self.is_empty()):
            raise EmptyStackException
        return self.top.value

    def pop(self):
        if(self.is_empty()):
            raise EmptyStackException

        returned_element = self.top.value
        self.top = self.top.previous

        return returned_element




