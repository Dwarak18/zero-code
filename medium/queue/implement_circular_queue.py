import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [0] * k
        self.k = k
        self.head = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        tail = (self.head + self.count) % self.k
        self.q[tail] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.k
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        tail = (self.head + self.count - 1) % self.k
        return self.q[tail]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k

from measure_performance import measure_performance

@measure_performance
def test_MyCircularQueue():
    passed = 0
    total = 0
    # Test 1
    q = MyCircularQueue(3)
    res = [q.enQueue(1), q.enQueue(2), q.enQueue(3), q.enQueue(4), q.Rear(), q.isFull(), q.deQueue(), q.enQueue(4), q.Rear()]
    expected = [True, True, True, False, 3, True, True, True, 4]
    total += 1
    if res == expected:
        print(f"Test case 1 passed.")
        passed += 1
    else:
        print(f"Test case 1 failed: expected={expected}, got={res}")
    # Test 2
    q = MyCircularQueue(2)
    res = [q.enQueue(2), q.enQueue(3), q.enQueue(4), q.Front(), q.Rear(), q.isFull(), q.deQueue(), q.Front(), q.Rear(), q.isEmpty()]
    expected = [True, True, False, 2, 3, True, True, 3, 3, False]
    total += 1
    if res == expected:
        print(f"Test case 2 passed.")
        passed += 1
    else:
        print(f"Test case 2 failed: expected={expected}, got={res}")
    # Test 3
    q = MyCircularQueue(1)
    res = [q.enQueue(1), q.enQueue(2), q.Front(), q.Rear(), q.isFull(), q.deQueue(), q.isEmpty()]
    expected = [True, False, 1, 1, True, True, True]
    total += 1
    if res == expected:
        print(f"Test case 3 passed.")
        passed += 1
    else:
        print(f"Test case 3 failed: expected={expected}, got={res}")
    # Test 4
    q = MyCircularQueue(5)
    res = [q.isEmpty(), q.isFull(), q.enQueue(10), q.enQueue(20), q.enQueue(30), q.enQueue(40), q.enQueue(50), q.isFull(), q.Rear(), q.Front(), q.deQueue(), q.Front()]
    expected = [True, False, True, True, True, True, True, True, 50, 10, True, 20]
    total += 1
    if res == expected:
        print(f"Test case 4 passed.")
        passed += 1
    else:
        print(f"Test case 4 failed: expected={expected}, got={res}")
    # Test 5
    q = MyCircularQueue(2)
    res = [q.isEmpty(), q.enQueue(1), q.enQueue(2), q.isFull(), q.deQueue(), q.enQueue(3), q.Rear()]
    expected = [True, True, True, True, True, True, 3]
    total += 1
    if res == expected:
        print(f"Test case 5 passed.")
        passed += 1
    else:
        print(f"Test case 5 failed: expected={expected}, got={res}")
    print(f"Passed {passed}/{total} test cases.")

if __name__ == "__main__":
    test_MyCircularQueue()
