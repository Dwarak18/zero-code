import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
import heapq

class Solution:
    def minCostToSupplyWater(self, n, wells, pipes):
        graph = [[] for _ in range(n+1)]
        for i, w in enumerate(wells):
            graph[0].append((w, i+1))
            graph[i+1].append((w, 0))
        for u, v, w in pipes:
            graph[u].append((w, v))
            graph[v].append((w, u))
        visited = [False] * (n+1)
        min_heap = [(0, 0)]
        res = 0
        while min_heap:
            cost, u = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            res += cost
            for w, v in graph[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v))
        return res if all(visited) else -1

    def test_minCostToSupplyWater(self):
        test_cases = [
            (3, [1,2,2], [(1,2,1),(2,3,1)], 3),
            (2, [1,1], [(1,2,1)], 2),
            (2, [1,2], [(1,2,1)], 2),
            (3, [1,2,2], [(1,2,1),(2,3,2)], 3),
            (3, [1,2,2], [(1,2,1),(2,3,1)], 3),
            (4, [1,2,2,3], [(1,2,1),(2,3,1),(3,4,1)], 4),
            (4, [1,2,2,3], [(1,2,1),(2,3,1),(3,4,1),(1,4,1)], 4),
            (4, [1,2,2,3], [(1,2,1),(2,3,1),(3,4,1),(1,4,1),(2,4,1)], 4),
            (4, [1,2,2,3], [(1,2,1),(2,3,1),(3,4,1),(1,4,1),(2,4,1),(3,1,1)], 4),
            (4, [1,2,2,3], [(1,2,1),(2,3,1),(3,4,1),(1,4,1),(2,4,1),(3,1,1),(4,2,1)], 4),
            (4, [1,2,2,3], [(1,2,1),(2,3,1),(3,4,1),(1,4,1),(2,4,1),(3,1,1),(4,2,1),(1,3,1)], 4),
            (4, [1,2,2,3], [(1,2,1),(2,3,1),(3,4,1),(1,4,1),(2,4,1),(3,1,1),(4,2,1),(1,3,1),(2,1,1)], 4),
            (4, [1,2,2,3], [(1,2,1),(2,3,1),(3,4,1),(1,4,1),(2,4,1),(3,1,1),(4,2,1),(1,3,1),(2,1,1),(3,2,1)], 4),
            (4, [1,2,2,3], [(1,2,1),(2,3,1),(3,4,1),(1,4,1),(2,4,1),(3,1,1),(4,2,1),(1,3,1),(2,1,1),(3,2,1),(4,3,1)], 4),
            (4, [1,2,2,3], [(1,2,1),(2,3,1),(3,4,1),(1,4,1),(2,4,1),(3,1,1),(4,2,1),(1,3,1),(2,1,1),(3,2,1),(4,3,1),(1,2,1)], 4),
            (4, [1,2,2,3], [(1,2,1),(2,3,1),(3,4,1),(1,4,1),(2,4,1),(3,1,1),(4,2,1),(1,3,1),(2,1,1),(3,2,1),(4,3,1),(1,2,1),(2,3,1)], 4),
            (4, [1,2,2,3], [(1,2,1),(2,3,1),(3,4,1),(1,4,1),(2,4,1),(3,1,1),(4,2,1),(1,3,1),(2,1,1),(3,2,1),(4,3,1),(1,2,1),(2,3,1),(3,4,1)], 4),
            (4, [1,2,2,3], [(1,2,1),(2,3,1),(3,4,1),(1,4,1),(2,4,1),(3,1,1),(4,2,1),(1,3,1),(2,1,1),(3,2,1),(4,3,1),(1,2,1),(2,3,1),(3,4,1),(4,1,1)], 4),
        ]
        passed = 0
        for idx, (n, wells, pipes, expected) in enumerate(test_cases, 1):
            result = self.minCostToSupplyWater(n, wells, pipes)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({n}, {wells}, {pipes}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_minCostToSupplyWater()

if __name__ == "__main__":
    run_tests()
