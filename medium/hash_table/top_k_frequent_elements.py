import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        return [item for item, _ in heapq.nlargest(k, count.items(), key=lambda x: x[1])]

    def test_topKFrequent(self):
        test_cases = [
            ([1,1,1,2,2,3], 2, [1,2]),
            ([1], 1, [1]),
            ([1,2], 2, [1,2]),
            ([1,2,2,3,3,3], 1, [3]),
            ([1,2,2,3,3,3], 2, [3,2]),
            ([1,2,2,3,3,3], 3, [3,2,1]),
            ([4,1,-1,2,-1,2,3], 2, [-1,2]),
            ([1,1,2,2,3,3,4,4,5,5], 3, [1,2,3]),
            ([1,1,1,2,2,3,3,3,4,4,4,4], 1, [4]),
            ([1,1,1,2,2,3,3,3,4,4,4,4], 2, [4,1]),
            ([1,1,1,2,2,3,3,3,4,4,4,4], 3, [4,1,3]),
            ([1,2,3,4,5,6,7,8,9,10], 5, [1,2,3,4,5]),
            ([1,2,3,4,5,6,7,8,9,10], 10, [1,2,3,4,5,6,7,8,9,10]),
            ([1,2,3,4,5,6,7,8,9,10], 1, [1]),
            ([1,1,2,2,3,3,4,4,5,5], 5, [1,2,3,4,5]),
            ([1,1,2,2,3,3,4,4,5,5], 4, [1,2,3,4]),
            ([1,1,2,2,3,3,4,4,5,5], 3, [1,2,3]),
            ([1,1,2,2,3,3,4,4,5,5], 2, [1,2]),
            ([1,1,2,2,3,3,4,4,5,5], 1, [1]),
        ]
        passed = 0
        for idx, (nums, k, expected) in enumerate(test_cases, 1):
            result = self.topKFrequent(nums, k)
            if set(result) == set(expected) and len(result) == len(expected):
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({nums}, {k}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_topKFrequent()

if __name__ == "__main__":
    run_tests()
