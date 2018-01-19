from double_ended_queue import Doubly_LinkedQueue
import unittest


class DblQueueTest(unittest.TestCase):

    def test_init(self):
        q = Doubly_LinkedQueue()
        assert q.front() is None
        assert q.length() == 0
        assert q.is_empty() is True

    def test_init_with_list(self):
        q = Doubly_LinkedQueue(['A', 'B', 'C'])
        assert q.front() == 'A'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_length(self):
        q = Doubly_LinkedQueue()
        assert q.length() == 0
        q.enqueue_back('A')
        assert q.length() == 1
        q.enqueue_front('B')
        assert q.length() == 2
        q.dequeue_front('C')
        assert q.length() == 1
        q.dequeue_back()
        assert q.length() == 0

    def test_enqueue(self):
        q = Doubly_LinkedQueue()
        q.enqueue_back('B')
        assert q.front() == 'B'
        assert q.length() == 1
        q.enqueue_back('C')
        assert q.front() == 'B'
        assert q.length() == 2
        q.enqueue_front('A')
        assert q.front() == 'A'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_front_back(self):
        q = Doubly_LinkedQueue()
        assert q.front() is None
        q.enqueue_back('A')
        assert q.front() == 'A'
        q.enqueue_back('B')
        assert q.front() == 'A'
        q.enqueue_front()
        assert q.front() == 'B'
        q.enqueue_back()
        q.enqueue_front('C')
        assert q.front() == 'C'
        q.enqueue_front('B')
        assert q.front() == 'B'
        q.enqueue_front('A')
        assert q.front() == 'A'
        assert q.back() == 'C'
        q.enqueue_front()
        assert q.front() == 'B'
        assert q.back() == 'C'
        q.enqueue_front()
        q.enqueue_front()
        assert q.front() is None
        assert q.back() is None



if __name__ == '__main__':
    unittest.main()
