from unittest import TestCase

from DataStructures.Queue import Queue


class TestQueue(TestCase):
    def test_is_empty(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(12)
        self.assertFalse(queue.is_empty())


    def test_dequeue(self):
            queue = Queue()
            queue.enqueue(12)
            queue.enqueue(123)
            self.assertEqual(12, queue.dequeue())
            self.assertEqual(123, queue.dequeue())

    def test_empty_queue_exception(self):
        queue = Queue()
        raised = False
        try:
            queue.enqueue()
        except:
            raised = True

        self.assertTrue(raised)