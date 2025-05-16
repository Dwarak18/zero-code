import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
import heapq

class Solution:
    def scheduleCourse(self, courses):
        courses.sort(key=lambda x: x[1])
        heap = []
        total = 0
        for t, d in courses:
            total += t
            heapq.heappush(heap, -t)
            if total > d:
                total += heapq.heappop(heap)
        return len(heap)

    def test_scheduleCourse(self):
        test_cases = [
            ([[100,200],[200,1300],[1000,1250],[2000,3200]], 3),
            ([[1,2]], 1),
            ([[3,2],[4,3]], 0),
            ([[5,5],[4,6],[2,6]], 2),
            ([[1,2],[2,3],[3,4],[4,5]], 4),
            ([[5,5],[4,6],[2,6],[1,7]], 3),
            ([[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]], 4),
            ([[9,14],[7,12],[1,11],[4,7]], 3),
            ([[5,5],[4,6],[2,6],[1,7],[3,8]], 4),
            ([[1,2],[2,3],[3,4],[4,5],[5,6]], 5),
            ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]], 6),
            ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8]], 7),
            ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9]], 8),
            ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10]], 9),
            ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,11]], 10),
            ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,11],[11,12]], 11),
            ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,11],[11,12],[12,13]], 12),
            ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,11],[11,12],[12,13],[13,14]], 13),
            ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,11],[11,12],[12,13],[13,14],[14,15]], 14),
            ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,11],[11,12],[12,13],[13,14],[14,15],[15,16]], 15),
        ]
        passed = 0
        for idx, (courses, expected) in enumerate(test_cases, 1):
            result = self.scheduleCourse(courses)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={courses}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_scheduleCourse()

if __name__ == "__main__":
    run_tests()
