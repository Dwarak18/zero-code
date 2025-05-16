import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

# Simulate the guess API
class GuessGame:
    def __init__(self, pick):
        self.pick = pick
    def guess(self, num):
        if num == self.pick:
            return 0
        elif num < self.pick:
            return 1
        else:
            return -1

class Solution(GuessGame):
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            res = self.guess(mid)
            if res == 0:
                return mid
            elif res < 0:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def test_guess_number(self):
        test_cases = [
            (10, 6), (1, 1), (100, 99), (50, 25), (1000, 1), (1000, 1000), (500, 250), (500, 499), (2, 2), (2, 1),
            (20, 10), (20, 20), (20, 1), (100, 50), (100, 1), (100, 100), (100, 75), (100, 25), (100, 99), (100, 2)
        ]
        passed = 0
        for idx, (n, pick) in enumerate(test_cases, 1):
            sol = Solution(pick)
            result = sol.guessNumber(n)
            if result == pick:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {result}, expected {pick}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    Solution(1).test_guess_number()

if __name__ == "__main__":
    run_tests()
