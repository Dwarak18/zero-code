import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                start = i + 1
                total = 0
        return start

    def test_canCompleteCircuit(self):
        test_cases = [
            ([1,2,3,4,5], [3,4,5,1,2], 3),
            ([2,3,4], [3,4,3], -1),
            ([5,1,2,3,4], [4,4,1,5,1], 4),
            ([1,2,3,4,5], [5,4,3,2,1], 0),
            ([2,3,4], [3,4,3], -1),
            ([3,3,4], [3,4,4], -1),
            ([4,5,2,6,5,3], [3,2,7,3,2,9], 3),
            ([1,2,3,4,5], [1,2,3,4,5], 0),
            ([1,2,3,4,5], [2,3,4,5,1], 4),
            ([2,2,2], [2,2,2], 0),
            ([2,2,2], [2,2,3], -1),
            ([2,2,2], [3,2,2], 1),
            ([2,2,2], [2,3,2], 2),
            ([2,2,2], [2,2,3], -1),
            ([2,2,2], [3,2,2], 1),
            ([2,2,2], [2,3,2], 2),
            ([1,2,3,4,5], [3,4,5,1,2], 3),
            ([1,2,3,4,5], [2,3,4,5,1], 4),
            ([1,2,3,4,5], [1,2,3,4,5], 0),
            ([1,2,3,4,5], [5,4,3,2,1], 0),
        ]
        passed = 0
        for idx, (gas, cost, expected) in enumerate(test_cases, 1):
            result = self.canCompleteCircuit(gas, cost)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({gas}, {cost}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_canCompleteCircuit()

if __name__ == "__main__":
    run_tests()
