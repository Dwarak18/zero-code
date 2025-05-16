import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]
        for x_start, x_end in points[1:]:
            if x_start > end:
                arrows += 1
                end = x_end
        return arrows

    def test_findMinArrowShots(self):
        test_cases = [
            ([[10,16],[2,8],[1,6],[7,12]], 2),
            ([[1,2],[3,4],[5,6],[7,8]], 4),
            ([[1,2],[2,3],[3,4],[4,5]], 2),
            ([[1,2]], 1),
            ([[2,3],[2,3]], 1),
            ([[1,10],[2,3],[4,5],[6,7],[8,9]], 5),
            ([[1,10],[2,3],[4,5],[6,7],[8,9],[1,2]], 5),
            ([[1,10],[2,3],[4,5],[6,7],[8,9],[1,2],[2,3]], 5),
            ([[1,10],[2,3],[4,5],[6,7],[8,9],[1,2],[2,3],[3,4]], 5),
            ([[1,10],[2,3],[4,5],[6,7],[8,9],[1,2],[2,3],[3,4],[4,5]], 5),
            ([[1,10],[2,3],[4,5],[6,7],[8,9],[1,2],[2,3],[3,4],[4,5],[5,6]], 5),
            ([[1,10],[2,3],[4,5],[6,7],[8,9],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]], 5),
            ([[1,10],[2,3],[4,5],[6,7],[8,9],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8]], 5),
            ([[1,10],[2,3],[4,5],[6,7],[8,9],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9]], 5),
            ([[1,10],[2,3],[4,5],[6,7],[8,9],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10]], 5),
            ([[1,10],[2,3],[4,5],[6,7],[8,9],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,11]], 6),
            ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,11]], 5),
            ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,11],[11,12]], 6),
            ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,11],[11,12],[12,13]], 7),
            ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,11],[11,12],[12,13],[13,14]], 8),
        ]
        passed = 0
        for idx, (points, expected) in enumerate(test_cases, 1):
            result = self.findMinArrowShots(points)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={points}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_findMinArrowShots()

if __name__ == "__main__":
    run_tests()
