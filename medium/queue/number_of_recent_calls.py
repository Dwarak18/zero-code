import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

@measure_performance
def test_RecentCounter():
    passed = 0
    total = 0
    rc = RecentCounter()
    res = [rc.ping(1), rc.ping(100), rc.ping(3001), rc.ping(3002)]
    expected = [1,2,3,3]
    total += 1
    if res == expected:
        print(f"Test case 1 passed.")
        passed += 1
    else:
        print(f"Test case 1 failed: expected={expected}, got={res}")
    rc = RecentCounter()
    res = [rc.ping(642), rc.ping(1849), rc.ping(4921), rc.ping(5936), rc.ping(5957)]
    expected = [1,2,1,2,3]
    total += 1
    if res == expected:
        print(f"Test case 2 passed.")
        passed += 1
    else:
        print(f"Test case 2 failed: expected={expected}, got={res}")
    rc = RecentCounter()
    res = [rc.ping(100), rc.ping(200), rc.ping(300), rc.ping(400), rc.ping(500), rc.ping(600), rc.ping(700), rc.ping(800), rc.ping(900), rc.ping(1000)]
    expected = [1,2,3,4,5,6,7,8,9,10]
    total += 1
    if res == expected:
        print(f"Test case 3 passed.")
        passed += 1
    else:
        print(f"Test case 3 failed: expected={expected}, got={res}")
    rc = RecentCounter()
    res = [rc.ping(1), rc.ping(3001), rc.ping(6001), rc.ping(9001)]
    expected = [1,2,2,2]
    total += 1
    if res == expected:
        print(f"Test case 4 passed.")
        passed += 1
    else:
        print(f"Test case 4 failed: expected={expected}, got={res}")
    rc = RecentCounter()
    res = [rc.ping(1), rc.ping(1000), rc.ping(2000), rc.ping(3000), rc.ping(4000), rc.ping(5000), rc.ping(6000), rc.ping(7000), rc.ping(8000), rc.ping(9000)]
    expected = [1,2,3,4,4,4,4,4,4,4]
    total += 1
    if res == expected:
        print(f"Test case 5 passed.")
        passed += 1
    else:
        print(f"Test case 5 failed: expected={expected}, got={res}")
    print(f"Passed {passed}/{total} test cases.")

if __name__ == "__main__":
    test_RecentCounter()
