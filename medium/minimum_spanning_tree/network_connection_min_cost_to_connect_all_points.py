import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
import heapq

class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = [False] * n
        min_heap = [(0, 0)]
        res = 0
        count = 0
        while min_heap and count < n:
            cost, u = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            res += cost
            count += 1
            for v in range(n):
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(min_heap, (dist, v))
        return res

    def test_minCostConnectPoints(self):
        test_cases = [
            ([[0,0],[2,2],[3,10],[5,2],[7,0]], 20),
            ([[3,12],[-2,5],[-4,1]], 18),
            ([[0,0],[1,1],[1,0],[-1,1]], 4),
            ([[0,0]], 0),
            ([[0,0],[1,1]], 2),
            ([[0,0],[1,0]], 1),
            ([[0,0],[0,1]], 1),
            ([[0,0],[1,1],[2,2]], 4),
            ([[0,0],[2,2],[3,10],[5,2],[7,0],[10,10]], 34),
            ([[0,0],[1,1],[2,2],[3,3],[4,4]], 8),
            ([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5]], 12),
            ([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]], 16),
            ([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7]], 20),
            ([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8]], 24),
            ([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9]], 28),
            ([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10]], 32),
            ([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10],[11,11]], 36),
            ([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10],[11,11],[12,12]], 40),
            ([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10],[11,11],[12,12],[13,13]], 44),
            ([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10],[11,11],[12,12],[13,13],[14,14]], 48),
        ]
        passed = 0
        for idx, (points, expected) in enumerate(test_cases, 1):
            result = self.minCostConnectPoints(points)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={points}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_minCostConnectPoints()

if __name__ == "__main__":
    run_tests()
