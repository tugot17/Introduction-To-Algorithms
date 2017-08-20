from unittest import TestCase
from DataStructures.Stack import Stack


class TestStack(TestCase):


    def test_push(self):
        stack = Stack()

        stack.push(22)

        self.assertFalse(stack.isEmpty())


    def test_peek(self):
        stack = Stack()
        stack.push(22)
        stack.push(32)
        stack.push(60)

        self.assertEqual(60, stack.peek())
        self.assertEqual(60, stack.peek())



    def test_pop(self):
        stack = Stack()
        stack.push(22)
        stack.push(32)
        stack.push(60)

        self.assertEqual(60, stack.pop())
        self.assertEqual(32, stack.pop())
