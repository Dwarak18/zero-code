import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        count = 0
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]
        return count

    def test_eraseOverlapIntervals(self):
        test_cases = [
            ([[1,2],[2,3],[3,4],[1,3]], 1),
            ([[1,2],[1,2],[1,2]], 2),
            ([[1,2],[2,3]], 0),
            ([[1,100],[11,22],[1,11],[2,12]], 2),
            ([[0,2],[1,3],[2,4],[3,5],[4,6]], 2),
            ([[1,5],[2,3],[3,4],[4,5]], 1),
            ([[1,2]], 0),
            ([[1,2],[2,3],[3,4],[4,5]], 0),
            ([[1,2],[2,3],[3,4],[1,3],[2,4]], 2),
            ([[1,2],[2,3],[3,4],[1,3],[2,4],[3,5]], 3),
            ([[1,2],[2,3],[3,4],[1,3],[2,4],[3,5],[4,6]], 4),
            ([[1,2],[2,3],[3,4],[1,3],[2,4],[3,5],[4,6],[5,7]], 5),
            ([[1,2],[2,3],[3,4],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8]], 6),
            ([[1,2],[2,3],[3,4],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9]], 7),
            ([[1,2],[2,3],[3,4],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8,10]], 8),
            ([[1,2],[2,3],[3,4],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8,10],[9,11]], 9),
            ([[1,2],[2,3],[3,4],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8,10],[9,11],[10,12]], 10),
            ([[1,2],[2,3],[3,4],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8,10],[9,11],[10,12],[11,13]], 11),
            ([[1,2],[2,3],[3,4],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8,10],[9,11],[10,12],[11,13],[12,14]], 12),
            ([[1,2],[2,3],[3,4],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8,10],[9,11],[10,12],[11,13],[12,14],[13,15]], 13),
        ]
        passed = 0
        for idx, (intervals, expected) in enumerate(test_cases, 1):
            result = self.eraseOverlapIntervals(intervals)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={intervals}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_eraseOverlapIntervals()

if __name__ == "__main__":
    run_tests()
